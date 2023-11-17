from django.shortcuts import render
from .models import Product, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

POSTS_PER_PAGE = 9

# Create your views here.
def product_view(request):
    
    product =Product.objects.all()
    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, POSTS_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(POSTS_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
        
    context = {
        "products": product,
        "tags":Tag.objects.all()
    }
    return render(request, "product/product.html", context)

def product_detail_view(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product':product,
    }
    return render(request, 'product/detail.html', context)

def category_list_view(request, tag_name):
    product = Product.objects.all().filter(category__id=tag_name)
    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, POSTS_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(POSTS_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    tag = Tag.objects.get(id=tag_name)
    context = {
        "products":product,
        'tag':tag
    }
    return render(request, "product/category.html", context)