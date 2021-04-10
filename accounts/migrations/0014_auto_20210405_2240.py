# Generated by Django 3.1.2 on 2021-04-05 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210403_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='feedbackDate',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 5, 22, 40, 57, 250704)),
        ),
    ]