# Generated by Django 3.1.7 on 2022-08-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20220814_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
