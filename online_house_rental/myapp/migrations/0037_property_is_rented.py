# Generated by Django 5.1.1 on 2025-01-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_rename_billingaddress_tokenpayment_billing_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
    ]
