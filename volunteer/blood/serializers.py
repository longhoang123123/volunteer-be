# blood/serializers.py
from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers

from app.models import User
from app.serializers import UserSerializer
from .models import Donor


class DonorCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    date_of_birth = serializers.CharField(required=True)

    class Meta:
        model = Donor
        fields = ['user_id', 'gender', 'date_of_birth', 'id_number', 'address', 'phone', 'blood_type', 'weight', 'donation_count']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(pk=user_id)
        validated_data['user'] = user
        date_of_birth = validated_data.pop('date_of_birth')
        validated_data["date_of_birth"] = datetime.strptime(date_of_birth, "%d-%m-%Y").date()
        donor = Donor.objects.create(**validated_data)
        self.send_otp_email(donor)
        return donor

    def send_otp_email(self, donor):
        donor_email = donor.user.email

        subject = "Xác nhận tài khoản"
        message = f"""
         Chào {donor.user.first_name} {donor.user.last_name},

         Cảm ơn bạn đã đăng ký tham gia vào trang web của chúng tôi.

         Đây là mã xác minh của bạn: {donor.user.otp}.

         Trân trọng,
         Đội ngũ hỗ trợ hiến máu
         """
        from_email = settings.EMAIL_HOST_USER

        send_mail(
            subject,
            message,
            from_email,
            [donor_email],
            fail_silently=False,
        )

class DonorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Donor
        fields = '__all__'


