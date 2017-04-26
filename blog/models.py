from django.db import models

def post_upload_location(instance, filename):
    return "/images/blog/{}/{}".format(instance.id, filename)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, help_text="Title for post, also used for url")
    content = models.TextField()
    header_image = models.ImageField(upload_to=post_upload_location)

    def getPath(self):
        return self.title.replace(" ", "-")
