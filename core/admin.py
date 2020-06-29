from django.contrib import admin
from .models import Barang, BarangOrder, Order, BillingAddress, BuktiBayar

# Register your models here.

admin.site.register(Barang)
admin.site.register(BarangOrder)
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(BuktiBayar)
