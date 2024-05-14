# Generated by Django 5.0.6 on 2024-05-13 17:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_profile_address_alter_profile_age_and_more'),
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patiante_treatments', to='accounts.profile')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='calendars.calendar')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_treatments', to='accounts.profile')),
            ],
        ),
    ]
