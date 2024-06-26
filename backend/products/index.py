from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [ 'title', 'description', 'price', 'user' ]
    tags = 'get_product_tags'

    settings = {
        "SearchableAttributes": ['title', 'description', 'price']
    }
