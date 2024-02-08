from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail, EmailMessage

from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    #permission_classes = (IsAuthenticated, )

    def perform_update(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save()
                instance.save()
                email = EmailMessage(
                    'Title',
                    'Hello',
                    'a@a.com',
                    ['bulatvaliullin0@gmail.com',],
                )
                email.send(fail_silently=False)
        except Exception as e:
            raise APIException(e)

    # def perform_create(self, serializer):
    #     try:
    #         with transaction.atomic():
    #             instance = serializer.save()
    #             instance.save()
    #
    #             job_params = {'db_id': instance.id}
    #
    #             transaction.on_commit(lambda: task_execute.delay(job_params))
    #     except Exception as e:
    #         raise APIException(e)
