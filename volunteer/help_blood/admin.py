from django.contrib import admin
from .models import BloodRecipient

@admin.register(BloodRecipient)
class BloodRecipientAdmin(admin.ModelAdmin):
    """
    Configure admin interface for BloodRecipient model.
    """
    list_display = ('full_name', 'blood_type', 'required_quantity', 'status', 'request_date', 'urgency_level')
    list_filter = ('blood_type', 'urgency_level', 'status')
    search_fields = ('full_name', 'contact_number', 'email')
    list_per_page = 5
