from datetime import datetime

from flask_mail import Mail, Message


def email(ip, app):
    mail = Mail(app)
    msg = Message('hello friend', sender='fsociety', recipients=['test@domain.com'])
    msg.body = f"{ip} has been blocked"
    mail.send(msg)
    return "Message sent!"


def add_column(db, model, ip, path):
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    entry = (model(ip, time, path))
    db.session.add(entry)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
