from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    # http://127.0.0.1:8000/product/
    path('', views.product_list, name="product_list"),
    # http://127.0.0.1:8000/product/detail/1/
    path('detail/<int:id>/', views.product_detail, name="product_detail"),
]
