# Generated by Django 4.0.4 on 2022-05-27 07:09

import client.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_name', models.UUIDField(default=client.models.new_uuid, primary_key=True, serialize=False, unique=True)),
                ('clean_session', models.BooleanField(default=True)),
                ('userdata', models.CharField(blank=True, default='none', max_length=1024)),
                ('client_description', models.CharField(blank=True, max_length=1024)),
                ('client_serial_number', models.CharField(blank=True, max_length=128)),
                ('client_mac_address', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DataOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('current_value', models.FloatField(blank=True)),
                ('one_minute_average', models.FloatField(blank=True)),
                ('five_minute_average', models.FloatField(blank=True)),
                ('thirty_minute_average', models.FloatField(blank=True)),
                ('client_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_output', to='client.client')),
            ],
        ),
    ]
