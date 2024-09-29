# Generated by Django 4.1.6 on 2024-09-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_adminm'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='area',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='property',
            name='baths',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='property',
            name='beds',
            field=models.IntegerField(default=0),
        ),
    ]