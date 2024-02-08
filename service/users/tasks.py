from celery import shared_task
from django.conf import settings
from django.core.mail import get_connection

from service.celery import app


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
def sample_task():
    print('Test123')
