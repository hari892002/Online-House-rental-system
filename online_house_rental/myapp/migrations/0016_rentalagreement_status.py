# Generated by Django 5.1.1 on 2024-10-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_property_monthly_rent_property_terms_and_conditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalagreement',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
