# Generated by Django 4.2.13 on 2024-07-03 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0008_alter_agesverification_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 3, 19, 52, 45, 835454)),
        ),
    ]
