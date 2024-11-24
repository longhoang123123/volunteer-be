from django.contrib import admin
from .models import BloodBank

@admin.register(BloodBank)
class BloodBankAdmin(admin.ModelAdmin):
    list_display = ('blood_type', 'quantity', 'expiry_date', 'quality_status', 'status')
    list_filter = ('blood_type', 'quality_status', 'status')
    search_fields = ('blood_type', 'storage_unit', 'source')
    list_per_page = 5
