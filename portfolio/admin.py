"""Handles the administration of the site"""
from django.contrib import admin
from django.db import models
from .models import Project, Client, Skill, Role, Type, GalleryItem
# Widgets
from .widgets.TinyMCE4 import TinyMCE4Widget
from django.contrib.admin.widgets import FilteredSelectMultiple

class GalleryItemInline(admin.TabularInline):
    """The inline editor for the Gallery items"""
    model = GalleryItem
    extra = 1

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    """Class to handle administration of Project Items"""
    icon = '<i class="material-icons">work</i>'
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE4Widget()},
    }
    list_display = ('title', 'path_name', 'url', 'project_type', 'client', 'completion_date', 'public')
    list_filter = ('project_type', 'roles', 'skills', 'client', 'public')
    search_fields = ('title', 'url', 'path_name')
    fieldsets = (
        (None, {
            'fields': ('title', 'path_name', 'url', 'starting_date', 'completion_date', 'public')
        }), ('Header Image', {
            'fields': ('image', 'image_height', 'image_width')
        }), ('Content', {
            'fields': ('short_description', 'description')
        }), ('Sorting', {
            'fields': ('project_type', 'roles', 'skills', 'client')
        })
    )
    inlines = [
        GalleryItemInline,
    ]

admin.site.register(Project, ProjectAdmin)

class ClientAdmin(admin.ModelAdmin):
    """Class to handle administration of Client Items"""
    icon = '<i class="material-icons">face</i>'
admin.site.register(Client, ClientAdmin)

class SkillAdmin(admin.ModelAdmin):
    """Class to handle administration of Skill Items"""
    icon = '<i class="material-icons">code</i>'
admin.site.register(Skill, SkillAdmin)

class RoleAdmin(admin.ModelAdmin):
    """Class to handle administration of Role Items"""
    icon = '<i class="material-icons">work</i>'
admin.site.register(Role, RoleAdmin)

class TypeAdmin(admin.ModelAdmin):
    """Class to handle administration of Type Items"""
admin.site.register(Type, TypeAdmin)
