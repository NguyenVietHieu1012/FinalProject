from django.shortcuts import render
from models import CategoryModel
from django.views.generic import ListView, DetailView


# Create your views here.

class CategoryListView(ListView):
    queryset = CategoryModel.objects.all()
    template_name = 'category/list.html'
    context_object_name = 'category_list'


class CategoryDetailView(DetailView):
    model = CategoryModel
    template_name = 'category/detail.html'
    context_object_name = 'category'
