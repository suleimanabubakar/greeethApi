from django.core.mail import send_mail

from django.conf import settings
from django.http import JsonResponse
import uuid
def send_email(recepient,message,subject):    
    send_mail(subject=subject,from_email=settings.EMAIL_HOST_USER,message=message,recipient_list=recepient,fail_silently=False)



def TokenTemplate(token,t_type):
    if t_type=="reset":    
        subject="Password Reset Token"
        message = "Reset Your Password \n"



    else:
        subject="Account Activation Token"
        message = "Activate Your Account \n"

    message += f"Use the code below \n {token}"

    return {'subject':subject,'message':message}



def generate_coupon():
  return  uuid.uuid4()