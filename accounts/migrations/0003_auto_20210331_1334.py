# Generated by Django 3.1.2 on 2021-03-31 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210330_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedbackDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 13, 34, 26, 836859)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 13, 34, 26, 836859)),
        ),
    ]
