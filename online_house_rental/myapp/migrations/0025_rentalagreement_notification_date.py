# Generated by Django 5.1.1 on 2024-10-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_delete_propertyvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalagreement',
            name='notification_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
