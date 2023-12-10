from django.db import models
from order.models import OrderModel
from product.models import ProductModel


# Create your models here.
class OrderDetailModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT)
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
