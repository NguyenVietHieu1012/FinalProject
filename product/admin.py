from django.contrib import admin
from .models import ProductModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price", "quantity", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["product_name"]


# Register your models here.
admin.site.register(ProductModel, ProductAdmin)
