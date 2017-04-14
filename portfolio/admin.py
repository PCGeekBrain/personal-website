"""Handles the administration of the site"""
from django.contrib import admin
from .models import Project, Client, Skill, Role, Type

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    """Class to handle administration of Project Items"""
    icon = '<i class="material-icons">work</i>'
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



