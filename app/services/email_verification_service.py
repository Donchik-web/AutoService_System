import os
import random
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox, QApplication


load_dotenv()

def connect_smtp_server(email: str, info: str, messages: dict, status: str):
    """Отправляет письмо с кодом на email"""
    server = os.getenv("SMTP_SERVER")
    sender_email = os.getenv('SMTP_EMAIL')
    password = os.getenv('SMTP_PASSWORD')

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = messages[status]['Subject']

    email_text = messages[status]['Text'] + " " + info + "!"

    # Отправка сообщения на email
    msg.attach(MIMEText(email_text, 'plain', 'utf-8'))

    # Отправка через SMTP
    with smtplib.SMTP_SSL(server, 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)
        return True


def submission_push_code(email_le: QLineEdit, btn: QPushButton, email_code_users: dict) -> None:
    """Формирует код подтверждения"""
    email = email_le.text().strip()
    if not email or "@" not in email:
        QMessageBox.warning(email_le.window(),"Ошибка", "Введите корректный e‑mail")
        return

    window = email_le.window()
    window.setEnabled(False)

    btn.setText("Отправка…")
    QApplication.processEvents() # обновляем, чтобы текст изменился

    generate_code = random.randint(100000, 999999)

    try:
        from app.email_messages import messages_to_email
        if connect_smtp_server(email, str(generate_code), messages_to_email, 'registration'):
            email_code_users[email] = generate_code
            QMessageBox.information(email_le.window(), "Код отправлен", f"Код подтверждения отправлен на {email}")
            print(email_code_users)
    except Exception as e:
        QMessageBox.warning(window, "Ошибка отправки", f"Не удалось отправить письмо: {str(e)}")
    finally:
        window.setEnabled(True) # разблокировка окна
        btn.setText("Отправить снова")