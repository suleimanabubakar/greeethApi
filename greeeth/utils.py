from time import strptime
from django.core.mail import send_mail
import requests
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime,date
import uuid
from datetime import datetime,time
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



def get_reverse_location(point):
    long,lat = point.coords

    params = {
        'q': f'{long},{lat}',
        'key':settings.GEO_REVERSE_KEY
    }

    return requests.get('https://api.opencagedata.com/geocode/v1/json',params=params)

def get_weather(point):
    long,lat = point.coords
    print(f'{long},{lat}')
    params = {
        'geocode': f'{long},{lat}',
        'format':'json',
        'units':'m',
        'language':'en-US',
        'apiKey':settings.WEATHER_API_KEY,
    }

    return requests.get('https://api.weather.com/v3/wx/forecast/daily/3day',params=params)


def timing():
    now_time = datetime.now().time()
    return "night"  if time(8, 00) <= now_time >= time(18, 00) else "day"

def convert_str_date(date):
    return datetime.strptime(date[:10],'%Y-%m-%d').date()
    



split = lambda x, n: [x[:n]] + [split(x[-(len(x) - n) :] if -(len(x) - n) else [], n)][0] if x else x