"""This file describes the Database object model for the Portfolio app"""
from django.db import models


class Type(models.Model):
    """Database Object Model for storing the types of projects"""
    name = models.CharField(max_length=30, help_text="Name of the type of project")
    slug = models.CharField(max_length=30, help_text="Used in URL", unique=True)
    description = models.CharField(max_length=200, help_text="For listing", blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/portfolio/type/' + self.slug


class Role(models.Model):
    """Database Object Model for storing the roles I've taken"""
    name = models.CharField(max_length=30, help_text="Name of position/role")
    slug = models.CharField(max_length=30, help_text="Used in URL", unique=True)
    description = models.CharField(max_length=200, help_text="For listing", blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/portfolio/role/' + self.slug


class Skill(models.Model):
    """Database Object Model for storing the skills used in the projects"""
    name = models.CharField(max_length=30, help_text="Name of skill")
    slug = models.CharField(max_length=30, help_text="Used in URL", unique=True)
    description = models.CharField(max_length=200, help_text="For listing", blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/portfolio/skill/' + self.slug

class Client(models.Model):
    """Database Object Model for storing the clients that the projects where done for"""
    name = models.CharField(max_length=100, help_text="Name of client to display")
    slug = models.CharField(max_length=50, help_text="Used in URL", unique=True)
    url = models.URLField(blank=True, help_text="URL to send viewer to")
    # Will add more fields for manageing clients later if wanted
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/portfolio/client/' + self.slug


class Project(models.Model):
    """Database Object Model for Projects on personal Portfolio"""
    title = models.CharField(max_length=35, help_text="Title for the project")
    # Path name is used in the URLS as some providers make an issue out or whitespace
    path_name = models.CharField(max_length=30, help_text="/projects/<path_name>", db_index=True)
    # an Image to make life nice. need to test
    image = models.ImageField(upload_to="portfolio/projects/", blank=True, null=True)
    # Description
    short_description = models.TextField(max_length=250)
    short_description.help_text = "250 character description of the project for the front page"
    description = models.TextField(help_text="Description displayed detail page")
    # Date Started - Ended (final optional)
    starting_date = models.DateField(null=True, blank=True, help_text="Optional date range")
    completion_date = models.DateField()
    # The URL of the project if there is one
    url = models.URLField(blank=True, null=True)
    # ForeignKey relationships to other tables for managemnet
    project_type = models.ForeignKey(Type, blank=True, null=True)
    roles = models.ManyToManyField(Role, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True)
    # Is it shown publicly
    public = models.BooleanField(default=True)

    # Internal Stats not shown to public
    created_at = models.DateTimeField(auto_now_add=True)
    last_modifed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/portfolio/project/' + self.path_name
