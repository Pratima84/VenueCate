# Generated by Django 3.1.2 on 2021-03-29 18:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingdate', models.DateField(auto_now_add=True)),
                ('guestNumber', models.IntegerField(blank=True)),
                ('eventStartDate', models.DateField()),
                ('eventEndDate', models.DateField()),
                ('eventType', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='extraService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(blank=True, max_length=200)),
                ('servicePrice', models.IntegerField(null=True)),
                ('catering', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.catering')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venueName', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('min_guestCapacity', models.IntegerField(blank=True, null=True)),
                ('max_guestCapacity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('website', models.URLField(blank=True, max_length=1000)),
                ('openTime', models.TimeField(blank=True, null=True)),
                ('closingTime', models.TimeField(blank=True, null=True)),
                ('addService', models.ManyToManyField(to='accounts.extraService')),
            ],
        ),
        migrations.CreateModel(
            name='venueImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('venue', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(help_text='Email', max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('profile_picture', models.ImageField(upload_to='accounts/static/images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentDate', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 30, 0, 19, 47, 185872))),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ManyToManyField(related_name='item', to='accounts.Category')),
            ],
        ),
        migrations.CreateModel(
            name='food_Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packageName', models.CharField(max_length=100)),
                ('price', models.IntegerField(null='False')),
                ('Menu_Items', models.ManyToManyField(related_name='Menu_Items', to='accounts.Menu_Items')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=1000)),
                ('feedbackDate', models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 30, 0, 19, 47, 186870))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.AddField(
            model_name='catering',
            name='packageType',
            field=models.ManyToManyField(related_name='food_Package', to='accounts.food_Package'),
        ),
        migrations.AddField(
            model_name='booking',
            name='catering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.catering'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AddField(
            model_name='booking',
            name='extraService',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.extraservice'),
        ),
        migrations.AddField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue'),
        ),
    ]
