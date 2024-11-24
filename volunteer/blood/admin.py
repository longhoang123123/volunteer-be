# blood/admin.py
from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_type', 'id_number', 'donation_count')
    search_fields = ('user__first_name', 'user__last_name', 'id_number', 'blood_type')
    list_filter = ('blood_type',)
    list_per_page = 5
