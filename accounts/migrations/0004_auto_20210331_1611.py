# Generated by Django 3.1.2 on 2021-03-31 10:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210331_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedbackDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 16, 11, 39, 206990)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 16, 11, 39, 205994)),
        ),
        migrations.CreateModel(
            name='OrderedFoodPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packageName', models.CharField(max_length=100)),
                ('price', models.IntegerField(null='False')),
                ('Menu_Items', models.ManyToManyField(to='accounts.Menu_Items')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='foodpackage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.orderedfoodpackage'),
        ),
    ]
