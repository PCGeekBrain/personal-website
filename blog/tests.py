"""Unit tests for blog"""
from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Post

# Create your tests here.
class PostTestCases(TestCase):
    """Test the Post class"""
    def setUp(self):
        Post.objects.create(title="Duplicate", slug="special")

    def test_auto_path_generation(self):
        """Test path generation when path not provided"""
        title = "Super long Title with Odd Chars{} in it?:"
        expectedResult = "super-long-title-with-odd-chars{}-in-it?:"
        Post.objects.create(title=title, slug="test")
        post1 = Post.objects.get(title=title)
        self.assertEqual(post1.path, expectedResult)

    def test_duplicate_posts(self):
        """Test for unique clause"""
        with self.assertRaises(IntegrityError):
            Post.objects.create(title="Duplicate", slug="special")
    
    def test_path_regex_bad(self):
        """Test coustom regex to invalidate on Capital Chars and spaces"""
        with self.assertRaises(ValidationError):
            post = Post(title="bad regex", path="Super-2Test-2", slug="special")
            if post.full_clean():
                post.save()

        with self.assertRaises(ValidationError):
            post = Post(title="bad regex", path="super-2test 2", slug="special")
            if post.full_clean():
                post.save()
        self.assertEqual(Post.objects.filter(title="bad regex").count(), 0)
    
    def test_path_regex_good(self):
        """Test odd chars in path"""
        Post.objects.create(title="good regex", path=":~`!@#$%^&*()-987+_=\\|[]{}\'", slug="test_9-5")
        self.assertEqual(Post.objects.filter(title="good regex").count(), 1)
