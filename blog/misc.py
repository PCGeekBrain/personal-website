"""Misc functions used in the blog"""
from django.conf import settings
import random
import os

class random_stock_image:
    def __init__(self):
        print('read folder')
        self.images = os.listdir(os.path.join(settings.BASE_DIR, 'common_static/stock_img'))
    def generate(self):
        return "/static/stock_img/{}".format(random.choice(self.images))
