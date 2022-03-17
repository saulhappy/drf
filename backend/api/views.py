from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product

def api_home(request, *args, **kwargs):
    random_product = Product.objects.all().order_by("?").first()
    if random_product:
        data = model_to_dict(random_product)
    return JsonResponse(data)
