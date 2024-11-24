from django.db import models

class BloodDonationEvent(models.Model):
    name = models.CharField(max_length=255, verbose_name="Event Name")
    description = models.TextField(blank=True, null=True, verbose_name="Event Description")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    location = models.CharField(max_length=255, verbose_name="Location")

    # Số lượng máu cần thu thập theo từng nhóm máu và Rh
    blood_goal_A_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (A+)")
    blood_goal_A_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (A-)")
    blood_goal_B_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (B+)")
    blood_goal_B_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (B-)")
    blood_goal_AB_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (AB+)")
    blood_goal_AB_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (AB-)")
    blood_goal_O_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (O+)")
    blood_goal_O_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Goal (O-)")

    # Số lượng máu đã thu thập theo từng nhóm máu và Rh
    blood_collected_A_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (A+)")
    blood_collected_A_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (A-)")
    blood_collected_B_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (B+)")
    blood_collected_B_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (B-)")
    blood_collected_AB_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (AB+)")
    blood_collected_AB_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (AB-)")
    blood_collected_O_positive = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (O+)")
    blood_collected_O_negative = models.PositiveIntegerField(default=0, verbose_name="Blood Collected (O-)")

    # Trạng thái sự kiện
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='upcoming',
        verbose_name="Status"
    )

    def __str__(self):
        return self.name
