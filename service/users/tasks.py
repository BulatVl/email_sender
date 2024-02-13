import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import get_connection, EmailMessage

from service.celery import app

from .models import CustomUser


@shared_task()
def async_send_messages_with_smtp(email_messages):
    conn = get_connection(backend=settings.EMAIL_BACKEND, fail_silently=False)
    if not email_messages:
        return 0
    with conn._lock:
        new_conn_created = conn.open()
        if not conn.connection or new_conn_created is None:
            return 0
        num_sent = 0
        for message in email_messages:
            sent = conn._send(message)
            if sent:
                num_sent += 1
        if new_conn_created:
            conn.close()
    return num_sent


@app.task()
def periodic_task():
    users = CustomUser.objects.filter(email_verified=True)
    for user in users:
        gmail = user.email
        payload = {'lat': user.lat, 'lon': user.lon, 'appid': '9b7ed7e896b027f1071a31769bbbefa9'}
        r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
        print(r.json(), payload)
        text = 'Temperature: ' + str(r.json()['main']['temp'] - 273.15) + '\n' + 'Weather: ' + r.json()['weather'][0]['description']
        email = EmailMessage(
            'Title',
            text,
            'a@a.com',
            [gmail, ],
        )
        email.send(fail_silently=False)
