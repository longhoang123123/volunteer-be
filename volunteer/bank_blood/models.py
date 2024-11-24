from django.db import models

class BloodBank(models.Model):
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

    STATUS_CHOICES = [
        ('Good', 'Good'),
        ('Expired', 'Expired'),
        ('Contaminated', 'Contaminated'),
    ]

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, verbose_name="Blood Type")
    quantity = models.PositiveIntegerField(verbose_name="Quantity (ml)")
    donation_date = models.DateField(verbose_name="Donation Date")
    expiry_date = models.DateField(verbose_name="Expiry Date")
    quality_status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name="Quality Status")
    storage_unit = models.CharField(max_length=50, verbose_name="Storage Unit", blank=True, null=True) # Lưu thông tin vị trí lưu trữ máu trong kho
    storage_condition = models.CharField(max_length=255, verbose_name="Storage Condition", blank=True, null=True) #Lưu điều kiện bảo quản (ví dụ: "Nhiệt độ thấp", "Kho lạnh").
    source = models.CharField(max_length=255, verbose_name="Source of Blood", blank=True, null=True) #Ghi lại nguồn cung cấp máu (ví dụ: "Hiến tặng tại sự kiện XYZ").
    blood_used = models.PositiveIntegerField(verbose_name="Blood Used (ml)", default=0)
    status = models.CharField(max_length=20, choices=[('In Stock', 'In Stock'), ('Used', 'Used'), ('Disposed', 'Disposed')], default='In Stock')

    def __str__(self):
        return f"{self.blood_type} - {self.quantity}ml"

    @property
    def is_expired(self):
        """Kiểm tra máu đã hết hạn hay chưa"""
        from datetime import date
        return date.today() > self.expiry_date
