# Generated by Django 2.2.8 on 2020-06-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='kategori',
            field=models.CharField(choices=[('S', 'Snack'), ('D', 'Drink'), ('P', 'Produk')], default='S', max_length=1),
            preserve_default=False,
        ),
    ]
