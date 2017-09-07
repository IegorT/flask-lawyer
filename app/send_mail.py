from flask_mail import Message
from flask import render_template
from app import mail, app
from app.dec import async
from config import ADMINS


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body.encode()
    msg.html = html_body.encode()
    send_async_email(app, msg)


def question_mail(name, phone, email, message):
    send_mail("From site", ADMINS[0], ADMINS,
              render_template('question_mail.txt', name=name, phone=phone, email=email, msg=message),
              render_template('question_mail.html', name=name, phone=phone, email=email, msg=message))
