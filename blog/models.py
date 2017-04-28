from django.db import models
from django.core.validators import RegexValidator, validate_slug
from django.utils import timezone

def post_upload_location(instance, filename):
    return "images/blog/{}/{}".format(instance.image_folder, filename)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=25, db_index=True, validators=[validate_slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

# Create your models here.
class Post(models.Model):
    """The block of content detailing the post"""
    title = models.CharField(max_length=150, help_text="Title for post, also used for url")
    path = models.CharField(max_length=150, help_text="\"/blog/posts/...\" Will be autofilled from title. No spaces or Uppercase", unique=True, validators=[
        RegexValidator(regex='^[^\sA-Z]+$', message="Lowercase with no whitespace allowed")
    ], blank=True)
    content = models.TextField(blank=True, null=True)
    header_image = models.ImageField(upload_to=post_upload_location, blank=True, null=True, height_field="image_height", width_field="image_width")
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image_folder = models.CharField(max_length=15, default="unsorted")
    # sorting
    category = models.ManyToManyField(Category, blank=True)
    # allows for automated releasing
    publish_date = models.DateTimeField(verbose_name="Publish At:", default=timezone.now)
    # Internal Stats not shown to public
    created_at = models.DateTimeField(auto_now_add=True)
    last_modifed = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.path:
            self.path = self.title.lower().replace(' ', '-') #replace the whitespace in the url
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
