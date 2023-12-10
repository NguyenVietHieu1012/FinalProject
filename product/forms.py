from django import forms
from .models import ProductModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductForm(forms.Form):
    product_name = forms.CharField(label="Tên sản phẩm", max_length=100, required=True)
    summary = forms.CharField(label="Tóm tắt", max_length=500)
    description = forms.CharField(label="Mô tả chi tiết", widget=forms.Textarea)
    price = forms.IntegerField(label="Giá")
    quantity = forms.IntegerField(label="Số lượng")

    def save(self):
        model = ProductModel(
            product_name=self.cleaned_data["product_name"],
            summary=self.cleaned_data["summary"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            quantity=self.cleaned_data["quantity"],
        )
        model.save()


class ProductModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta():
        model = ProductModel
        fields = '__all__'
