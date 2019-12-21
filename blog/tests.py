from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User


# Create your tests here.
class HomeViewTests(TestCase):
    def setUp(self):
        """# Create an auth user for creating post"""
        User.objects.create_user(username='testcase-user', email='testcase-user@bogusemail.com',
                                 password='ayoola4321')

    def retrieve_auth_user_posts(self):
        """Retrieve the created authenicated user and create two posts with the user"""
        user = User.objects.get_by_natural_key('testcase-user')
        user.post_set.create(title='This is for test', content='Test content that I am using')
        user.post_set.create(title='This is for test - post 2', content='Test content that I am using - post 2')
        posts = user.post_set.all()
        return posts

    def test_posts(self):
        self.assertQuerysetEqual(self.retrieve_auth_user_posts(), ['<Post: This is for test>',
                                                                   '<Post: This is for test - post 2>'], ordered=False)

    def test_view_with_posts(self):
        """Check what the home view returns with two created posts by one author"""
        posts = self.retrieve_auth_user_posts()
        response = self.client.post(reverse('blog:blog_home'))
        self.assertQuerysetEqual(response.context['posts'], ['<Post: This is for test>',
                                                             '<Post: This is for test - post 2>'], ordered=False)

    def test_context_entries(self):
        posts = self.retrieve_auth_user_posts()
        response = self.client.post(reverse('blog:blog_home'))
        self.assertEqual(response.context['posts'].get(title='This is for test'), posts.get(title='This is for test'))
        self.assertEqual(response.context['posts'].get(title='This is for test - post 2'),
                         posts.get(title='This is for test - post 2'))

    def test_first_post_fields(self):
        posts = self.retrieve_auth_user_posts()
        response = self.client.post(reverse('blog:blog_home'))
        self.assertEqual(response.context['posts'].get(title='This is for test').title, 'This is for test')
        self.assertEqual(response.context['posts'].get(title='This is for test').content,
                         'Test content that I am using')
        self.assertEqual(response.context['posts'].get(title='This is for test').author,
                         posts.get(pk=1).author)

    def test_second_post_fields(self):
        posts = self.retrieve_auth_user_posts()
        response = self.client.post(reverse('blog:blog_home'))
        self.assertEqual(response.context['posts'].get(title='This is for test - post 2').title,
                         'This is for test - post 2')
        self.assertEqual(response.context['posts'].get(title='This is for test - post 2').content,
                         'Test content that I am using - post 2')
        self.assertEqual(response.context['posts'].get(title='This is for test - post 2').author,
                         posts.get(pk=2).author)

    def tearDown(self):
        User.objects.get_by_natural_key('testcase-user').delete()
