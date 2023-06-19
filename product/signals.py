from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from .models import Product


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.product_image.delete(False)
    
@receiver(post_save, sender=Product)
def save_compressed_img(sender, instance, *args, **kwargs):
    size = 600, 600
    image=instance.product_image
    if image:
        product_image = Image.open(image.path)
        try:
            product_image.thumbnail(size, Image.LANCZOS)
            product_image.save(image.path)
        except:
            if product_image.mode in ("RGBA", "P"):
                product_img = product_image.convert("RGB")
                product_img.thumbnail(size, Image.LANCZOS)
                product_img.save(image.path)
                