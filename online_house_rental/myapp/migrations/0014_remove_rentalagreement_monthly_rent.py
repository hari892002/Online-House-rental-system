# Generated by Django 5.1.1 on 2024-10-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_rentalagreement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalagreement',
            name='monthly_rent',
        ),
    ]
