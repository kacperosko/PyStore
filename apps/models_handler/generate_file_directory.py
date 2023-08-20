import os
import re
from datetime import datetime


def file_directory_path(name, filename, object_name):
    ext = filename.split('.')[-1]
    now = datetime.now()
    filename = "%s_%s.%s" % (re.sub('[^a-zA-Z0-9]+', '', name), now.strftime("%H%M_%d%m%Y"), ext)
    return os.path.join(f'{object_name}_images',
                        "{0}_{1}".format(object_name, re.sub('[^a-zA-Z0-9]+', '', name)),
                        filename)


def generate_product_path(instance, filename):
    return file_directory_path(name=instance.name, filename=filename, object_name='product')


def generate_post_path(instance, filename):
    return file_directory_path(name=instance.title, filename=filename, object_name='post')
