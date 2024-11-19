from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="arta",
            password="9378"
        )

        self.blog = Blog.objects.create(
            title="Test Title",
            text="Test Text",
            author=self.user,
        )

    # test the title to show in admin pannel
    def test_blog_showing_name(self):
        blog = Blog(title="Test title for show")
        self.assertEqual(str(blog), blog.title)

    def test_blog_model(self):
        self.assertEqual(self.blog.title, "Test Title")
        self.assertEqual(self.blog.text, "Test Text")
        self.assertEqual(str(self.blog.author), "arta")

    def test_blog_list_view(self):
        res = self.client.get(reverse("blogs"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "blog/blogs.html")

    def test_create_blog(self):
        res = self.client.post(reverse('new_blog'), {
            "title": "test create blog",
            "text": "test text blog",
            "author": self.user.id
        })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Blog.objects.last().title, "test create blog")
        self.assertEqual(Blog.objects.last().text, "test text blog")

    def test_blog_edit(self):
        res = self.client.post(reverse('update_blog', args="1"), {
            "title": "edited Title",
            "text": "edited Text"
        })
        self.assertEqual(res.status_code, 302)