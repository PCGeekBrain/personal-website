from django.contrib import admin
from django.db import models
from .models import Post, Category
from .widgets.TinyMCE4 import TinyMCE4Widget
from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """Class to handle administration of Project Items"""
    icon = '<i class="material-icons">work</i>'
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE4Widget()},
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Roles/Skills", False)}
    }
    list_display = ('title', 'path', 'publish_date', 'created_at', 'last_modifed')
    list_filter = ('category',)

admin.site.register(Post, PostAdmin)

admin.site.register(Category)
