# Generated by Django 3.0.1 on 2020-01-16 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0012_fee_property_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Transaction'),
        ),
    ]
