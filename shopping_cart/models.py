import auto_prefetch
from django.db import models
from django.db.models import Sum
from digital_marketplace.utils.models import TimeBasedModel
from digital_marketplace.utils.choices import OrderStatus, PaymentStatus
# Create your models here.

class Order(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        "home.CustomUser",
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=15,
        choices=OrderStatus.choices, 
        default=OrderStatus.Pending
    )
    items = models.ManyToManyField("shopping_cart.OrderItem", blank=True)
    ref_code = models.CharField(max_length=50, blank=True)

    def get_total(self):
        return self.items.all().aggregate(order_total=Sum("book__price"))['order_total']

    def __str__(self):
        return f"{self.user} Order"
    

class OrderItem(TimeBasedModel):
    book = auto_prefetch.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.book.name
    
class Payment(TimeBasedModel):
    order = auto_prefetch.ForeignKey(
        "shopping_cart.Order",
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=50, 
        choices=PaymentStatus.choices,
        default=PaymentStatus.Pending
    )
    total_amount = models.FloatField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    raw_response = models.TextField(blank=True)


    def __str__(self):
        return f"{self.order} - {self.transaction_id} Payment"
    