from django.db import models
from category.models import CategoryModel
from ckeditor.fields import RichTextField
import os


# Create your models here.

class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, null=True)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(default=0)

    description = RichTextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_flg = models.BooleanField(null=True)
    image = models.ImageField(null=True, upload_to="images/")

    def __str__(self):
        return self.product_name

    @property
    def get_file_name(self):
        return os.path.basename(self.file.url) if self.file else ""
