# Generated by Django 5.1.1 on 2024-10-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rentalagreement_owner_digital_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='terms_and_conditions',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]