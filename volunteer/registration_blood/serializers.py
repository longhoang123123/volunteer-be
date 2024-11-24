from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from blood.serializers import DonorSerializer
from event_blood.serializers import BloodDonationEventSerializer
from .models import Donor, BloodDonationEvent, DonorRegistration

class DonorRegistrationSerializer(serializers.ModelSerializer):
    donor = DonorSerializer()  # Hiển thị thông tin người hiến máu
    event = BloodDonationEventSerializer()  # Hiển thị thông tin sự kiện hiến máu

    class Meta:
        model = DonorRegistration
        fields = ['id', 'donor', 'event', 'registration_date', 'status']


class DonorRegistrationCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    event_id = serializers.IntegerField(required=True)

    class Meta:
        model = DonorRegistration
        fields = ['user_id', 'event_id']

    def validate(self, data):
        user_id = data.pop('user_id')
        event_id = data.pop('event_id')

        # Kiểm tra xem đối tượng Donor và BloodDonationEvent có tồn tại không
        donor = Donor.objects.get(user__id=user_id) if user_id else None
        event = BloodDonationEvent.objects.get(id=event_id) if event_id else None

        # Nếu không tìm thấy donor hoặc event, raise exception
        if not donor:
            raise serializers.ValidationError("Donor not found.")
        if not event:
            raise serializers.ValidationError("Event not found.")

        data['donor'] = donor
        data['event'] = event
        return data

    def create(self, validated_data):
        donor_registration = DonorRegistration.objects.create(**validated_data)
        self.send_confirmation_email(donor_registration)
        return donor_registration

    def send_confirmation_email(self, donor_registration):

        donor_email = donor_registration.donor.user.email
        event_name = donor_registration.event.name
        registration_date = donor_registration.registration_date

        subject = "Xác nhận đăng ký hiến máu"
        message = f"""
        Chào {donor_registration.donor.user.first_name} {donor_registration.donor.user.last_name},

        Cảm ơn bạn đã đăng ký tham gia hiến máu tại sự kiện "{event_name}" vào ngày {registration_date}.

        Chúng tôi rất biết ơn sự đóng góp của bạn và hy vọng sự kiện sẽ thành công tốt đẹp.

        Trân trọng,
        Đội ngũ hỗ trợ hiến máu
        """
        from_email = settings.EMAIL_HOST_USER

        send_mail(
            subject,
            message,
            from_email,
            [donor_email],  # Gửi email cho người hiến máu
            fail_silently=False,
        )
