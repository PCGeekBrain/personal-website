"""Unit tests for blog"""
from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import timedelta
from django.utils import timezone
from .models import Post

# Create your tests here.
class PostTestCases(TestCase):
    """Test the Post class"""
    def setUp(self):
        Post.objects.create(title="Duplicate")

    def test_auto_path_generation(self):
        """Test path generation when path not provided"""
        title = "Super long Title with Odd Chars{} in it?:"
        expectedResult = "super-long-title-with-odd-chars{}-in-it?:"
        Post.objects.create(title=title)
        post1 = Post.objects.get(title=title)
        self.assertEqual(post1.path, expectedResult)

    def test_duplicate_posts(self):
        """Test for unique clause"""
        with self.assertRaises(IntegrityError):
            Post.objects.create(title="Duplicate")
    
    def test_path_regex_bad(self):
        """Test coustom regex to invalidate on Capital Chars and spaces"""
        with self.assertRaises(ValidationError):
            post = Post(title="bad regex", path="Super-2Test-2")
            if post.full_clean():
                post.save()

        with self.assertRaises(ValidationError):
            post = Post(title="bad regex", path="super-2test 2")
            if post.full_clean():
                post.save()
        self.assertEqual(Post.objects.filter(title="bad regex").count(), 0)
    
    def test_path_regex_good(self):
        """Test odd chars in path"""
        Post.objects.create(title="good regex", path=":~`!@#$%^&*()-987+_=\\|[]{}\'")
        self.assertEqual(Post.objects.filter(title="good regex").count(), 1)


class PostSiteTestCases(TestCase):
    """Unit tests for the rendered site"""
    def setUp(self):
        Post.objects.create(title="Post 1", publish_date=timezone.now() + timedelta(5))
        Post.objects.create(title="Post 2")
        Post.objects.create(title="Post 3", publish_date=timezone.now() - timedelta(6))
        Post.objects.create(title="Post 4", publish_date=timezone.now() - timedelta(5))

    def test_recent_contains(self):
        client = Client()
        post1 = Post.objects.get(path='post-1')
        post2 = Post.objects.get(path='post-2')
        recent = client.get('/blog/')
        self.assertNotContains(recent, post1)
        self.assertContains(recent, post2)

    def test_recent_contains(self):
        posts = [Post.objects.get(path='post-2'), Post.objects.get(path='post-4'), Post.objects.get(path='post-3'), ]
        response = Client().get('/blog/')
        for i in range(len(posts)):
            self.assertEqual(response.context['posts'][i], posts[i])
