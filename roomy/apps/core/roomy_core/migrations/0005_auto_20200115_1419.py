# Generated by Django 3.0.1 on 2020-01-15 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0004_fee_fee_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='time_stamp',
            field=models.DateTimeField(),
        ),
    ]
