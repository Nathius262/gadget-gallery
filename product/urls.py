from django.urls import path, include
from .views import *

app_name = "product"

urlpatterns = [
    path("", product_view, name="product"),
    path("tag/<int:tag_name>/", category_list_view, name="tag"),
    path('detail/<int:pk>/', product_detail_view, name='product_detail'),
]