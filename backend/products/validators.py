from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from products.models import Product


unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")
