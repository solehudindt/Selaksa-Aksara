# Generated by Django 2.2.8 on 2020-06-28 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200628_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buktibayar',
            name='user',
        ),
    ]
