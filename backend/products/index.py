from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = ["user", "title", "content", "price", "is_public"]
