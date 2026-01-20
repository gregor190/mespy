import smtplib
from email.mime.text import MIMEText

class MeSpy:
    def __init__(self, smtp_server="smtp.gmail.com", port=465):
        self.smtp_server = smtp_server
        self.port = port
        self.server = None
        self.email = None

    def set_credentials(self, email, password):
        """Login with your email + password (or app password)."""
        self.server = smtplib.SMTP_SSL(self.smtp_server, self.port)
        self.server.login(email, password)
        self.email = email

    def send(self, to, subject, body):
        """Send a plain text email."""
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.email
        msg["To"] = to
        self.server.sendmail(self.email, to, msg.as_string())

    def close(self):
        """Close the connection."""
        if self.server:
            self.server.quit()
