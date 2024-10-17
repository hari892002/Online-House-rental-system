# Generated by Django 5.1.1 on 2024-10-15 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_user_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='property_videos/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='myapp.property')),
            ],
        ),
    ]