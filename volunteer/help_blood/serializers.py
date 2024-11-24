from rest_framework import serializers
from .models import BloodRecipient

class BloodRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRecipient
        fields = '__all__'
