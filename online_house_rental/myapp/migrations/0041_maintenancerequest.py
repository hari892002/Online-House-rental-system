# Generated by Django 5.1.1 on 2025-01-22 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_alter_property_is_rented'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='maintenance_images/')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('emergency', 'Emergency')], default='low', max_length=20)),
                ('status', models.CharField(choices=[('reported', 'Reported'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('declined', 'Declined')], default='reported', max_length=20)),
                ('reported_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('owner_notes', models.TextField(blank=True, null=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('notification_date', models.DateTimeField(blank=True, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_requests', to='myapp.user')),
            ],
        ),
    ]
