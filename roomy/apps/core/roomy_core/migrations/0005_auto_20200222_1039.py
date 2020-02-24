# Generated by Django 3.0.3 on 2020-02-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0004_auto_20200222_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='status',
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.IntegerField(choices=[(0, 'Available(Solo)'), (1, 'Available(Shared)'), (2, 'Unavailable')], default=0),
        ),
    ]
