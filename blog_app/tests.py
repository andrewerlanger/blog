from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):

  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='testuser',
      email='test@example.com',
      password='secret',
  )

    self.post = Post.objects.create(
      title='test title',
      body='body of content',
      author=self.user,
    )

  def test_string_representation(self):
    post = Post(title="sample title")

    self.assertEqual(str(post), post.title)

  def test_post_content(self):
    self.assertEqual(self.post.title, 'test title')
    self.assertEqual(self.post.body, 'body of content')
    self.assertEqual(self.post.author.username, 'testuser')

  def test_post_list_view(self):

    # same as self.client.get('') -> which is 'home' reversed...
    response = self.client.get(reverse('home'))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'body of content')
    self.assertTemplateUsed('home.html')

  def test_post_detail_view(self):

    response = self.client.get('/post/1/')

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'body of content')
    self.assertTemplateUsed('post_detail.html')

  def test_post_no_response(self):

    response = self.client.get('/post/2/')

    self.assertEqual(response.status_code, 404)

