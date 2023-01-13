from django import template
from shopping_cart.models import Order
from digital_marketplace.utils.choices import OrderStatus

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, status=OrderStatus.Pending)
        if qs.exists():
            return qs[0].items.count()
    return 0
