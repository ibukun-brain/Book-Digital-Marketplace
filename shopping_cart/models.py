import auto_prefetch
from django.db import models
from django.db.models import Sum
from digital_marketplace.utils.models import TimeBasedModel
from digital_marketplace.utils.choices import OrderStatus
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
    items = models.ManyToManyField("shopping_cart.OrderItem")
    ref_code = models.CharField(max_length=50)

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
    total_amount = models.FloatField()
    transaction_ref = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.order} - {self.transaction_id}"
    