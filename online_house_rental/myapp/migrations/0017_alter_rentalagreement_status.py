# Generated by Django 5.1.1 on 2024-10-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rentalagreement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalagreement',
            name='status',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
