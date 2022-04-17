from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return f"{round(float(self.price) * .97, 2)}"

    def get_discount(self):
        return f"3%"
