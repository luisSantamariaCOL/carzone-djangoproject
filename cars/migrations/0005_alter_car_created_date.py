# Generated by Django 3.2 on 2023-07-16 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20230715_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 15, 19, 19, 59, 310713)),
        ),
    ]