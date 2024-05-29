import random
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

PRODUCTS_TAGS_LIST = ('cars', 'electronics', 'jets', 'shoes')

class Product(models.Model):
    user  = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=33.99)
    public = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    def is_public(self) -> bool:
        return self.public
    
    def get_product_tags(self):
        return random.choice(PRODUCTS_TAGS_LIST)


    @property
    def calculate_discount(self):
        return "%.02f" %(float(self.price) * 0.4)
    
    def get_title(self):
        return self.title

