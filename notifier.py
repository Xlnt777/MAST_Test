from email.mime.text import MIMEText
from email.header import Header
from config import DEBUG


def notify(name: str, url: str, text: str):
    if DEBUG == "True":
        _mock_notify(name, url, text)
    else:
        _smtp_notify(name, url, text)


def _mock_notify(name: str, url: str, text: str):
    print("\n=== EMAIL ===")
    print(name)
    print(url)
    print()
    print(text)
    print("============\n")



def _smtp_notify(name: str, url: str, text: str):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    from config import (
        SMTP_HOST,
        SMTP_PORT,
        SMTP_USE_TLS,
        SMTP_USERNAME,
        SMTP_PASSWORD,
        EMAIL_FROM,
        EMAIL_TO,
    )

    subject = f"Новая запись: {name}"
    body = f"{name}\n\n{url}\n\n{text}"

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = EMAIL_FROM
    msg["To"] = ", ".join(EMAIL_TO)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        if SMTP_USE_TLS:
            server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())






