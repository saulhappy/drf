from rest_framework import generics

from backend.products.models import Product

from backend.products.serializers import ProductSerializer

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serilizer_class = ProductSerializer