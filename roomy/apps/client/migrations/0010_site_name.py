# Generated by Django 3.0.1 on 2020-01-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_externallink_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(default='Roomy', max_length=32),
            preserve_default=False,
        ),
    ]
