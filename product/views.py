from django.shortcuts import render
from .models import Product, Tag
from django.shortcuts import get_object_or_404

# Create your views here.
def product_view(request):
    context = {
        "products":Product.objects.all(),
        "tags":Tag.objects.all()
    }
    return render(request, "product/product.html", context)


def category_list_view(request, tag_name):
    product = get_object_or_404(Product, tag_name)
    print(product)
    return render(request, "product/category.html")