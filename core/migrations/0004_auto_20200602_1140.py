# Generated by Django 2.2.8 on 2020-06-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200602_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='kategori',
            field=models.CharField(choices=[('Snack', 'S'), ('Drink', 'D'), ('Produk', 'P')], max_length=6),
        ),
    ]
