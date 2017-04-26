from django.contrib import admin
from django.db import models
from .models import Post
from .widgets.TinyMCE4 import TinyMCE4Widget

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """Class to handle administration of Project Items"""
    icon = '<i class="material-icons">work</i>'
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE4Widget()},
    }
    list_display = ('title', 'slug')
    list_filter = ('slug',)

admin.site.register(Post, PostAdmin)
