from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    # auto_now_add <- time when it created
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.product_name