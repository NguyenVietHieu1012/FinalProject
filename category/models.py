from django.db import models


# Create your models here.

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(null=True)

    def __str__(self):
        return self.category_name
