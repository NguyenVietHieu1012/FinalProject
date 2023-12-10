from django.db import models
from customer.models import CustomerModel


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT)
    order_number = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    description = models.CharField(max_length=200, null=True)
    ordered_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number
