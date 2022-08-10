from django.core.mail import EmailMessage

from django.conf import settings
from django.http import JsonResponse

def send_email(recepient,message,subject):    
    EmailMessage(subject=subject,from_email=settings.EMAIL_HOST_USER,body=message,
                        to=recepient)



def TokenTemplate(token,t_type):
    if t_type=="reset":    
        subject="Password Reset Token"
        message = "Reset Your Password \n"



    else:
        subject="Account Activation Token"
        message = "Activate Your Account \n"

    message += f"Use the code below \n {token}"

    return {'subject':subject,'message':message}