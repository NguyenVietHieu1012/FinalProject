from django.urls import path
from . import views

app_name = "category"

urlpatterns = [
    # http://127.0.0.1:8000/category/
    path('', views.CategoryListView.as_view(), name="category_list"),
    # http://127.0.0.1:8000/category/1/
    path('<int:pk>', views.CategoryDetailView.as_view(), name="category_detail"),
]