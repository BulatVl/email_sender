from rest_framework import serializers

from .models import CustomUser

import phonenumbers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'telegram', 'phone')
        read_only_fields = ('pk', 'email_verified', 'telegram_verified', 'phone_verified')

    # def validate_phone(self, value):
    #     if not phonenumbers.is_valid_number(value):
    #         raise serializers.ValidationError('We need a valid phonenumber')
    #     return value
