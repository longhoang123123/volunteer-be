from rest_framework import serializers

from app.models import User
from registration_blood.models import DonorRegistration
from .models import BloodDonationEvent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DonorRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = DonorRegistration
        fields = '__all__'

    def get_user(self, obj):
        return UserSerializer(obj.donor.user).data


class BloodDonationEventSerializer(serializers.ModelSerializer):
    registrations = serializers.SerializerMethodField()

    class Meta:
        model = BloodDonationEvent
        fields = '__all__'

    def get_registrations(self, obj):
        return DonorRegistrationSerializer(obj.events.all(), many=True).data
