from django.test import TestCase
from .models import Post

# Create your tests here.
class PostURLTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Test Title", slug="test")

    def test_path_title_conversion(self):
        post1 = Post.objects.get(title="Test Title")
        post1_path = post1.getPath()
        self.assertEqual(post1.title, post1.getTitle(post1_path))
