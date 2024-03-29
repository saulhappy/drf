from random import choice
from django.conf import settings
from django.db import models
from django.db.models import Q


User = settings.AUTH_USER_MODEL
EXPENSIVE_PRODUCT_PRICE = 50
PRODUCT_MODEL_TAGS = ["cereal", "chocolate", "candy"]


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(is_public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    title = models.CharField(
        max_length=120
    )  # imagine we later want to call this "name", to the outside world, but want to leave it in the model...
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    is_public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def path(self):
        return f"/products/{self.pk}/"

    # exposes "title" as "name"
    @property
    def name(self):
        return self.title

    def __str__(self):
        return f"{self.title}"

    def is_expensive_item(self):
        return self.price > EXPENSIVE_PRODUCT_PRICE

    def get_random_model_tag(self):
        return [choice(PRODUCT_MODEL_TAGS)]

    @property
    def sale_price(self):
        return f"{round(float(self.price) * .97, 2)}"

    def get_discount(self):
        return f"3%"
