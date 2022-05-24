from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = "is_expensive_item"
    fields = ["user", "title", "content", "price", "is_public"]
    tags = 'get_random_model_tag'
