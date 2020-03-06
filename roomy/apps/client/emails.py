from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def ContactUs_Handler(name,email,phone_number,message):
    try:
        subject = "ROOMY MANAGEMENT - WEBSITE MESSAGES/FEEDBACK"
        message = f"NAME: {name}\nEMAIL: {email}\nPHONE_NUMBER: {phone_number}\nMESSAGE: {message}"
        email_from = settings.EMAIL_HOST_USER
        managers_email = User.objects.filter(groups__name='Staff').values_list('email',flat=True)

        send_mail( subject, message, email_from, managers_email )
        return "EMAIL SENT"
    except Exception as e:
        raise e
