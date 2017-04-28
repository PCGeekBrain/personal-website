"""Misc functions used in the blog"""
from django.conf import settings
import random
import os

def random_stock_image():
    return "/static/stock_img/{}".format(random.choice(settings.RANDOM_IMAGES))
