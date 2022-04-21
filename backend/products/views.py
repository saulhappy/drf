from requests import request
from rest_framework import generics, permissions
from api.mixins import StaffEditorPermissionMixin
from products.models import Product
from products.serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content, user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request
        user = self.request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDestroyAPIView.as_view()
