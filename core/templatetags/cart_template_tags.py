from django import template
from core.models import Order

register = template.Library()


@register.filter
def hitung_brg_cart(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, dipesan=False)
        if qs.exists():
            return qs[0].barangs.count()

    return 0
