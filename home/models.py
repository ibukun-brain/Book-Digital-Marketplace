from django.db import models
from django.contrib.auth.models import AbstractUser
from digital_marketplace.utils.managers import CustomUserManager



# Create your models here.
class CustomUser(AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    email = models.EmailField(unique=True, max_length=40)


    def __str__(self):
        return self.get_full_name() or self.email
    