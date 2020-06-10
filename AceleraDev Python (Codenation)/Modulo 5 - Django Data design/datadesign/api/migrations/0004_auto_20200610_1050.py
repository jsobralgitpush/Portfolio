# Generated by Django 3.0.7 on 2020-06-10 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200610_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.CharField(max_length=39, null=True, validators=[django.core.validators.validate_ipv4_address], verbose_name='address'),
        ),
    ]