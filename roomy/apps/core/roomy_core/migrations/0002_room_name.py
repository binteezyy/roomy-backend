# Generated by Django 3.0.1 on 2020-01-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomy_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=56),
            preserve_default=False,
        ),
    ]