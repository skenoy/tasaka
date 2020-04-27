from flask import render_template
from flask_mail import Message
from app import app, mail
from threading import Thread
from datetime import datetime


def async_send_mail(app, subject, to, template, kwargs):
    # 获取当前程序的上下文
    with app.app_context():
        # 实例化的message对象(subject,recipients,sender)
        msg = Message(
            subject=subject, recipients=to, sender=app.config["MAIL_USERNAME"]
        )
        # 重定向到某个html
        msg.html = render_template("email/" + template + ".html", **kwargs)
        time = datetime.now()
        msg.date = time.timestamp()
        # 邮件发送
        mail.send(message=msg)


def email(subject, to, template, **kwargs):
    # thread代表发送邮件的线程信息
    thread = Thread(target=async_send_mail, args=(app, subject, to, template, kwargs))
    thread.start()