# Generated by Django 5.1.1 on 2025-01-28 16:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_delete_videosession'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('furniture', 'Furniture'), ('appliances', 'Appliances'), ('electronics', 'Electronics'), ('kitchenware', 'Kitchenware'), ('decor', 'Home Decor'), ('other', 'Other')], max_length=50)),
                ('condition', models.CharField(choices=[('new', 'New'), ('like_new', 'Like New'), ('good', 'Good'), ('fair', 'Fair'), ('used', 'Used')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('warranty_info', models.TextField(blank=True, null=True)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.property')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='household_items', to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='household_items/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.householditem')),
            ],
        ),
    ]
