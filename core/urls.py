from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    IndexView,
    BarangDetailView,
    add_to_cart,
    CheckoutView,
    remove_from_cart,
    remove_single,
    OrderSumView,
    adminOrderView,
    inputBukti,
)

app_name = 'core'
urlpatterns = [
    path('orders/', adminOrderView, name='orders'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-sum', OrderSumView.as_view(), name='order-sum'),
    path('produk/<slug>/', BarangDetailView.as_view(), name='produk'),
    path('add-to-cart/<slug>/', add_to_cart, name='addtocart'),
    path('rmv-from-cart/<slug>/', remove_from_cart, name='rmv-from-cart'),
    path('rmv-single/<slug>/', remove_single, name='rmv-single'),
    path('input-bukti/', inputBukti, name='inputBukti'),
    path('', IndexView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
