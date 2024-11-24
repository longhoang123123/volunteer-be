from django.contrib import admin
from .models import DonorRegistration

class DonorRegistrationAdmin(admin.ModelAdmin):
    list_display = ['donor', 'event', 'registration_date', 'status']
    list_filter = ['status', 'event__name', 'donor']
    search_fields = ['donor__user__first_name', 'donor__user__last_name', 'event__name', 'donor__blood_type']
    list_per_page = 5

admin.site.register(DonorRegistration, DonorRegistrationAdmin)
