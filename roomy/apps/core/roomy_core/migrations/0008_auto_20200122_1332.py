# Generated by Django 3.0.1 on 2020-01-22 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0007_auto_20200122_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.RoomCatalog', unique=True),
        ),
    ]
