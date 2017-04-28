"""Misc functions used in the blog"""
import random
from django.conf import settings

def random_stock_image():
    """Returns the url to a random stock image from the common static folder"""
    return "/static/stock_img/{}".format(random.choice(settings.RANDOM_IMAGES))
