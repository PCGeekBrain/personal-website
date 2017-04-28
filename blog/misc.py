"""Misc functions used in the blog"""
from django.conf import settings
import random
import os

def random_stock_image():
    images = os.listdir(os.path.join(settings.BASE_DIR, 'common_static/stock_img'))
    return "/static/stock_img/{}".format(random.choice(images))
