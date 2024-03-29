from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from products.validators import unique_product_title

from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    # title = serializers.CharField(validators=[unique_product_title])
    name = serializers.CharField(source="title")

    class Meta:
        model = Product
        fields = [
            "user_id",
            "owner",
            "pk",
            "url",
            "edit_url",
            "name",
            "price",
            "sale_price",
            "my_discount",
            "path",
        ]

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.id}, request=request)

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None

    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f" From serializer: {value} already exists."
            )
        return value
