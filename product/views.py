from django.http import HttpResponse
from django.shortcuts import render
from .models import ProductModel
from .forms import ProductModelForm
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.conf import settings
from category.models import CategoryModel


# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def product_list(request):
    # return render(request, 'product/list.html')
    category_list = CategoryModel.objects.all()
    limit = request.GET.get("limit")
    if limit and limit.isnumeric():
        limit = int(limit)
    else:
        limit = settings.DEFAULT_LIMIT

    sort = request.GET.get("sort")
    page = request.GET.get("page", 1)
    if sort not in ["-created_at", "created_at", "product_name"]:
        sort = settings.DEFAULT_SORT
    keyword = request.GET.get("keyword")

    if keyword:
        product_list = ProductModel.objects.filter(Q(product_name__contains=keyword) | Q(description__contains=keyword))
    else:
        product_list = ProductModel.objects.all()

    product_list = product_list.order_by(sort)

    product_list_paging = Paginator(product_list, limit)
    try:
        product_list_paging = product_list_paging.get_page(page)
    except PageNotAnInteger:
        product_list_paging = product_list_paging.get_page(1)
    except EmptyPage:
        product_list_paging = product_list_paging.get_page(product_list_paging.num_pages)

    context = {
        "product_list": product_list_paging,
        "keyword": keyword if keyword else "",
        "category_list": category_list,
    }
    return render(request, 'product/list.html', context)


def product_detail(request, id):
    # return HttpResponse("<b>Product Detail Page </b>")

    product = ProductModel.objects.get(id=id)
    context = {
        "product": product,
    }
    return render(request, 'product/detail.html', context)
