# Generated by Django 3.0.3 on 2020-03-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='message',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='name',
            new_name='question',
        ),
    ]
