# blood/models.py
from django.contrib.auth import get_user_model
from django.db import models
from app.models import User
#from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Donor(models.Model):
    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ')
    ]

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='blood',
        unique=True,
    )
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    id_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    weight = models.DecimalField(max_digits=999, decimal_places=0)
    medical_history = models.TextField(blank=True, null=True)
    last_health_check_date = models.DateField(null=True, blank=True)
    health_check_result = models.TextField(blank=True, null=True)
    last_donation_date = models.DateField(null=True, blank=True)
    donation_count = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    donation_history = models.TextField(blank=True, null=True)
    willingness_to_participate = models.BooleanField(default=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.blood_type} - {self.id_number}"

    class Meta:
        verbose_name = "Người Hiến Máu"
        verbose_name_plural = "Người Hiến Máu"
