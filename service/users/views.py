from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated, )

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
