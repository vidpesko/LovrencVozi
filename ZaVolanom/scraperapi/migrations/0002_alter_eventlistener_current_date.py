# Generated by Django 5.1 on 2024-08-10 18:21

import scraperapi.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraperapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlistener',
            name='current_date',
            field=models.DateTimeField(validators=[scraperapi.validators.validate_event_date]),
        ),
    ]
