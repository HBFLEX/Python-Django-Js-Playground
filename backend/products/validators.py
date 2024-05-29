from rest_framework import serializers
from .models import Product



def validate_title(value):
    product = Product.objects.filter(title__iexact=value)
    if product.exists():
        raise serializers.ValidationError('product already added')
    return value


