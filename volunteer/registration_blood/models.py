from django.db import models

from blood.models import Donor
from event_blood.models import BloodDonationEvent


class DonorRegistration(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donors')
    event = models.ForeignKey(BloodDonationEvent, on_delete=models.CASCADE, related_name='events')
    registration_date = models.DateTimeField(auto_now_add=True)
    blood_donated = models.PositiveIntegerField(default=0, help_text="The amount of blood donated by the donor (in units).")
    status = models.CharField(max_length=20, choices=[('registered', 'Registered'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='registered')

    class Meta:
        unique_together = ['donor', 'event']  # Một người không thể đăng ký tham gia một sự kiện hai lần

    def __str__(self):
        return f"{self.donor.user.first_name} {self.donor.user.last_name} - {self.event.name}"

    def save(self, *args, **kwargs):
        # Đảm bảo trạng thái người đăng ký luôn hợp lệ
        if self.status == 'cancelled' and self.event.status == 'completed':
            raise ValueError("Cannot cancel registration for a completed event")
        super().save(*args, **kwargs)
