# Generated by Django 3.1.2 on 2021-03-10 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210307_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 21, 42, 53, 59632)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedbackDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 21, 42, 53, 61625)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 21, 42, 53, 60630)),
        ),
    ]
