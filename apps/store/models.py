from django.db import models
from django.conf import settings
from datetime import datetime
import os
import re
from django.dispatch import receiver


def file_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.now()
    filename = "%s_%s.%s" % (re.sub('[^a-zA-Z0-9]+', '', instance.name), now.strftime("%H%M_%d%m%Y"), ext)
    return os.path.join('product_images',
                        "product_{0}".format(re.sub('[^a-zA-Z0-9]+', '', instance.name)),
                        filename)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=False)
    image = models.FileField(upload_to=file_directory_path)
    date_created = models.DateField(auto_now_add=True)

    quantity = None
    attributes = None

    class Meta:
        ordering = ('-date_created',)


class Attribute(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


class Product_Attribute(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attribute_product', null=False)
    id_attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='product_attribute_attribute', null=False)


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
