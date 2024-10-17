# Generated by Django 5.1.1 on 2024-10-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_rentalagreement_monthly_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='monthly_rent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='terms_and_conditions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]