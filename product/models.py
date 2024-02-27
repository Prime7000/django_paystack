from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

class Place_order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_amount = models.IntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    delivery_address = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

