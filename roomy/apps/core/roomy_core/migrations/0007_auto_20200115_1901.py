# Generated by Django 3.0.1 on 2020-01-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0006_auto_20200115_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]