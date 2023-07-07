from django.db import models

class OrderStatus(models.TextChoices):
    Pending = ("pending", "pending")
    Completed = ("completed", "completed")


class PaymentStatus(models.TextChoices):
    Pending = ("pending", "Pending")
    Successful = ("successful", "Successful")
    Failed = ("failed", "Failed")


class BookStatus(models.TextChoices):
    Owned = ("owned", "owned")
    In_cart = ("in_cart", "in_cart")
    Not_in_cart = ("not_in_cart", "not_in_cart")