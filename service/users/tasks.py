from celery import shared_task

from .models import CustomUser

@shared_task()
def task_execute(job_params):
    user = CustomUser.objects.get(id=job_params['db_id'])
    user.phone = 322832283228
    user.save()