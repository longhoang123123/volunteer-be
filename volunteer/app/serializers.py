import random

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
#from django.serializers import UserCreateSerializers # type: ignore
from rest_framework import serializers


User = get_user_model()

class UserVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        otp = attrs.get('otp')
        user = User.objects.get(email=email)
        if user.otp != otp:
            raise serializers.ValidationError('OTP không chính xác.')
        user.is_active = True
        user.otp = random.randint(100000, 999999)
        user.save()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        hash_password = make_password(password)
        user = User.objects.create_user(**validated_data, password=hash_password)
        user.otp = random.randint(100000, 999999)
        user.save()
        return user
