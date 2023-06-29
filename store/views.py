from django.shortcuts import render
from product.models import Tag, Product

# Create your views here.

def category_general_view(request):
    category_list = Tag.objects.all()
    context = {
        "category": category_list,
    }
    return context
def index_view(request):
    
    product = Product.objects.all()
    context = {
        "products": product
    }
    return render(request, "store/home.html", context)
