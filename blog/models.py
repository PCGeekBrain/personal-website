from django.db import models

def post_upload_location(instance, filename):
    return "images/blog/{}/{}".format(instance.slug, filename)

# Create your models here.
class Post(models.Model):
    """The block of content detailing the post"""
    title = models.CharField(max_length=150, help_text="Title for post, also used for url", unique=True)
    content = models.TextField(blank=True, null=True)
    header_image = models.ImageField(upload_to=post_upload_location, blank=True, null=True, height_field="image_height", width_field="image_width")
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    slug = models.CharField(max_length=30, db_index=True)

    def getPath(self):
        return self.title.replace(" ", "-")
    
    def getTitle(self, path):
        return path.replace("-", " ")
