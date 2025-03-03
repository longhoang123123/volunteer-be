# Generated by Django 5.0.7 on 2024-11-16 03:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BloodDonationEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Event Name")),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Event Description"
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Start Date")),
                ("end_date", models.DateField(verbose_name="End Date")),
                ("location", models.CharField(max_length=255, verbose_name="Location")),
                (
                    "blood_goal_A_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (A+)"
                    ),
                ),
                (
                    "blood_goal_A_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (A-)"
                    ),
                ),
                (
                    "blood_goal_B_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (B+)"
                    ),
                ),
                (
                    "blood_goal_B_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (B-)"
                    ),
                ),
                (
                    "blood_goal_AB_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (AB+)"
                    ),
                ),
                (
                    "blood_goal_AB_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (AB-)"
                    ),
                ),
                (
                    "blood_goal_O_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (O+)"
                    ),
                ),
                (
                    "blood_goal_O_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Goal (O-)"
                    ),
                ),
                (
                    "blood_collected_A_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (A+)"
                    ),
                ),
                (
                    "blood_collected_A_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (A-)"
                    ),
                ),
                (
                    "blood_collected_B_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (B+)"
                    ),
                ),
                (
                    "blood_collected_B_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (B-)"
                    ),
                ),
                (
                    "blood_collected_AB_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (AB+)"
                    ),
                ),
                (
                    "blood_collected_AB_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (AB-)"
                    ),
                ),
                (
                    "blood_collected_O_positive",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (O+)"
                    ),
                ),
                (
                    "blood_collected_O_negative",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Blood Collected (O-)"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("upcoming", "Upcoming"),
                            ("ongoing", "Ongoing"),
                            ("completed", "Completed"),
                        ],
                        default="upcoming",
                        max_length=10,
                        verbose_name="Status",
                    ),
                ),
            ],
        ),
    ]
