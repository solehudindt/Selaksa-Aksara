# Generated by Django 2.2.8 on 2020-06-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_barang_hrg_diskon'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='keterangan',
            field=models.TextField(blank=True),
        ),
    ]
