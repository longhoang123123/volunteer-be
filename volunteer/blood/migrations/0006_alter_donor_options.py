# Generated by Django 5.0.7 on 2024-11-20 14:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blood", "0005_remove_donor_registration_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="donor",
            options={
                "verbose_name": "Người Hiến Máu",
                "verbose_name_plural": "Người Hiến Máu",
            },
        ),
    ]
