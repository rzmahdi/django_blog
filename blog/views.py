from django.views.generic import ListView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"