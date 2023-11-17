from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.conf import settings
from .utils import image_location
from autoslug import AutoSlugField

# Create your models here.
class Tag(MPTTModel):
    tag_name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="product_parent")
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tag_name
    
    
class Product (models.Model):

    product_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=False)
    product_name = models.CharField(max_length=200, null=True)
    product_description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to=image_location, null=True, blank=True)
    category = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    slug = AutoSlugField(populate_from="product_name", unique=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        _ = "product"
        verbose_name = _
        verbose_name_plural = _+"s"
        ordering = [
            '-date',
            '-price',
            '-product_name',
        ]

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.pk])
        
    @property
    def image_url(self):
        try:
            url = self.product_image.url
        except:
            url = ""
            
        return url