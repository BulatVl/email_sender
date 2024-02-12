from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'telegram', 'phone', 'lat', 'lon')
        read_only_fields = ('pk', 'email_verified', 'telegram_verified', 'phone_verified')
