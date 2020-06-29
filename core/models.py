import uuid
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.text import slugify
import random

# Create your models here.

CATEGORY_PILIHAN = (
    ("Snack", "S"),
    ("Drink", "D"),
    ("Produk", "P")
)


def increment_invoice():
    invoice = 'SELAKSA' + str(random.randint(100, 100000))
    return invoice


class Barang(models.Model):
    judul = models.CharField(max_length=20)
    harga = models.FloatField()
    gambar = models.ImageField(upload_to='images/')
    hrg_diskon = models.FloatField(blank=True, null=True)
    kategori = models.CharField(choices=CATEGORY_PILIHAN, max_length=6)
    keterangan = models.TextField(blank=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("core:produk", kwargs={"slug": self.slug})

    def get_addtocart_url(self):
        return reverse("core:addtocart", kwargs={"slug": self.slug})

    def get_rmvfromcart_url(self):
        return reverse("core:rmv-from-cart", kwargs={"slug": self.slug})

    def __str__(self):
        return self.judul


class BarangOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=1)
    dipesan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.jumlah} {self.barang.judul}"

    def get_total_hrg(self):
        return self.jumlah * self.barang.harga

    def get_total_hrg_diskon(self):
        return self.jumlah * self.barang.hrg_diskon

    def get_hemat(self):
        return self.get_total_hrg() - self.get_total_hrg_diskon()

    def get_total_final(self):
        if self.barang.hrg_diskon:
            return self.get_total_hrg_diskon()
        return self.get_total_hrg()


class Order(models.Model):
    invoice = models.CharField(
        max_length=25, default=increment_invoice)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    barangs = models.ManyToManyField(BarangOrder)
    tgl = models.DateTimeField(auto_now=True)
    tgl_pesan = models.DateTimeField()
    dipesan = models.BooleanField(default=False)
    bayar = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.invoice
        # return f"{self.user.username} - {self.bukti_invo}"

    def get_total(self):
        total = 0
        for item in self.barangs.all():
            total += item.get_total_final()
        return total


class BuktiBayar(models.Model):
    invoice = models.CharField(max_length=13)
    foto = models.ImageField(upload_to='images/')


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    alamat = models.CharField(max_length=150)
    ket_lain = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=35)
    kode_pos = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user.username} - {self.kode_pos}"
