# Generated by Django 3.2 on 2023-07-17 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20230717_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 17, 11, 49, 45, 973505)),
        ),
    ]