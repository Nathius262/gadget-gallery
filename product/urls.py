from django.urls import path, include
from .views import *

app_name = "product"

urlpatterns = [
    path("", product_view, name="product"),
    path("tag/<str:tag_name>/", category_list_view, name="tag"),
]