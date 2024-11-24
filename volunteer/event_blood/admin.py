from django.contrib import admin

from registration_blood.models import DonorRegistration
from .models import BloodDonationEvent

@admin.register(BloodDonationEvent)
class BloodDonationEventAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'start_date',
        'end_date',
        'location',
        'status',
        'total_blood_goal',
        'total_blood_collected',
        'progress_percentage'
    )
    list_filter = ('status', 'start_date', 'end_date')  # Bộ lọc cho các trường
    search_fields = ('name', 'location')  # Tìm kiếm nhanh theo tên sự kiện và địa điểm
    list_per_page = 5

    def total_blood_goal(self, obj):

        return (
            obj.blood_goal_A_positive + obj.blood_goal_A_negative +
            obj.blood_goal_B_positive + obj.blood_goal_B_negative +
            obj.blood_goal_AB_positive + obj.blood_goal_AB_negative +
            obj.blood_goal_O_positive + obj.blood_goal_O_negative
        )
    total_blood_goal.short_description = 'Total Blood Goal (Units)'  # Tên hiển thị trong giao diện admin


    def total_blood_collected(self, obj):
        total_blood = DonorRegistration.objects.filter(event__id=obj.id, status='completed').count()
        return total_blood
    total_blood_collected.short_description = 'Total Blood Collected (Units)'

    def progress_percentage(self, obj):

        total_goal = self.total_blood_goal(obj)
        total_collected = self.total_blood_collected(obj)

        if total_goal > 0:
            progress = (total_collected / total_goal) * 100
            return f"{progress:.2f}%"  # Hiển thị dưới dạng phần trăm
        return "N/A"
    progress_percentage.short_description = 'Progress (%)'
