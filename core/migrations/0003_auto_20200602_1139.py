# Generated by Django 2.2.8 on 2020-06-02 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_barang_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='kategori',
            field=models.CharField(choices=[('S', 'Snack'), ('D', 'Drink'), ('P', 'Produk')], max_length=6),
        ),
    ]
