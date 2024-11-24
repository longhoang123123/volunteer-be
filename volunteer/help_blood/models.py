from django.db import models

class BloodRecipient(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    URGENCY_LEVELS = [
        ('Normal', 'Normal'), #Không khẩn cấp
        ('Urgent', 'Urgent'), #Yêu cầu cần được xử lý sớm
        ('Critical', 'Critical'), #Yêu cầu cực kỳ khẩn cấp
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'), #Yêu cầu đang chờ xử lý hoặc xét duyệt.
        ('Approved', 'Approved'), #Yêu cầu đã được phê duyệt
        ('Denied', 'Denied'), #Yêu cầu đã bị từ chối
        ('Completed', 'Completed'), #Yêu cầu đã hoàn thành
    ]

    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], verbose_name="Gender")
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    address = models.TextField(verbose_name="Address")

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, verbose_name="Blood Type")
    required_quantity = models.PositiveIntegerField(verbose_name="Required Quantity (ml)")
    urgency_level = models.CharField(max_length=10, choices=URGENCY_LEVELS, verbose_name="Urgency Level")
    medical_condition = models.TextField(blank=True, null=True, verbose_name="Medical Condition")

    request_date = models.DateField(auto_now_add=True, verbose_name="Request Date")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', verbose_name="Request Status")
    allocated_quantity = models.PositiveIntegerField(default=0, verbose_name="Allocated Quantity (ml)")
    allocation_date = models.DateField(blank=True, null=True, verbose_name="Allocation Date")

    assigned_hospital = models.CharField(max_length=255, blank=True, null=True, verbose_name="Assigned Hospital")
    doctor_in_charge = models.CharField(max_length=255, blank=True, null=True, verbose_name="Doctor In Charge")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    def __str__(self):
        return f"{self.full_name} ({self.blood_type})"

    class Meta:
        verbose_name = "Người Nhận Máu"
        verbose_name_plural = "Người Nhận Máu"
