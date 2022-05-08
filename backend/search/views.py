from rest_framework import generics

from backend.products.models import Product


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
