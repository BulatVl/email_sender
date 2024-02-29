from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'telegram', 'phone', 'lat', 'lon')
        read_only_fields = ('email_verified', 'telegram_verified', 'phone_verified')
