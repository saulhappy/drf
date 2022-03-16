from django.http import JsonResponse
from products.models import Product

def api_home(request, *args, **kwargs):
    random_product = Product.objects.all().order_by("?").first()
    data = {}
    if random_product:
        data["title"] = random_product.title
        data["content"] = random_product.content
        data["price"] = random_product.price
    return JsonResponse(data)
