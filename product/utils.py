import os
from django.conf import settings


def image_location(instance, filename):
    file_path = "product/{product_id}/{product_name}.jpeg".format(
        product_id = instance.product_owner, product_name =instance.product_name, filename=filename
    )
    
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        os.remove(full_path)
    return file_path