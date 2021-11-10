from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def sendEmail(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
