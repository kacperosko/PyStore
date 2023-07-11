from django.db import models
from django.conf import settings
from datetime import datetime
import os
import re
from django.dispatch import receiver
from apps.models_handler.generate_file_directory import generate_product_path


# def file_directory_path(instance, filename):
#     ext = filename.split('.')[-1]
#     now = datetime.now()
#     filename = "%s_%s.%s" % (re.sub('[^a-zA-Z0-9]+', '', instance.name), now.strftime("%H%M_%d%m%Y"), ext)
#     return os.path.join('product_images',
#                         "product_{0}".format(re.sub('[^a-zA-Z0-9]+', '', instance.name)),
#                         filename)


# def generate_product_url(instance):
#     url = '-'.join([re.sub(r'[\W_]+', '', word.lower()) for word in (re.sub(' +', ' ', instance.name)).split(" ")])
#     index = 0
#     while Product.objects.filter(url=url).exists():
#         url = '%s-%d' % (url, index)
#         index += 1
#     return url


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=False)
    url = models.CharField(unique=True, max_length=255, null=True, blank=True)
    image = models.FileField(upload_to=generate_product_path)
    date_created = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True, blank=False)

    quantity = None
    attributes = None

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_created',)

    def save(self, *args, **kwargs):
        """
        Overwrites Django 'save' function to generate unique url for each product
        """
        generated_url = '-'.join([re.sub(r'[\W_]+', '', word.lower()) for word in (re.sub(' +', ' ', self.name)).split(" ")])
        index = 0
        while Product.objects.filter(url=generated_url).exclude(id=self.id).exists():
            generated_url = '%s-%d' % (generated_url, index)
            index += 1
        self.url = generated_url

        super().save(*args, **kwargs)


class Attribute(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


class Product_Attribute(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attribute_product',
                                   null=False)
    id_attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='product_attribute_attribute',
                                     null=False)


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
