from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Very interesting Post')
        Post.objects.create(text='Very interesting Post Poland')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_value = 'Very interesting Post'

        self.assertEqual(expected_value, post.text)

    def test_contains_word(self):
        self.assertFalse(Post.objects.get(id=1).contains('Poland'))
        self.assertTrue(Post.objects.get(id=2).contains('Poland'))



class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Very interesting Post')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
