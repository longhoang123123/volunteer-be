from rest_framework import serializers
from .models import BloodBank

class BloodBankSerializer(serializers.ModelSerializer):
    is_expired = serializers.ReadOnlyField()

    class Meta:
        model = BloodBank
        fields = [
            'id', 'blood_type', 'quantity', 'donation_date', 'expiry_date',
            'quality_status', 'storage_unit', 'storage_condition', 'source',
            'blood_used', 'status', 'is_expired',
        ]
