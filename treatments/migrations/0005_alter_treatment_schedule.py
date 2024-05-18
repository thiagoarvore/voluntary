# Generated by Django 5.0.6 on 2024-05-18 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0006_alter_calendar_is_active'),
        ('treatments', '0004_alter_treatment_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='treatments', to='calendars.calendar'),
        ),
    ]
