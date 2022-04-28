from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    first_five_products = serializers.SerializerMethodField(read_only=True)

    def get_first_five_products(self, user):
        my_first_five_products_qs = user.product_set.all()[:5]
        return UserProductInlineSerializer(
            my_first_five_products_qs, many=True, context=self.context
        ).data
