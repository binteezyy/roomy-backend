# Generated by Django 3.0.1 on 2020-01-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0008_transaction_add_ons'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]