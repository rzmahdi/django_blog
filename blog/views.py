from django.views.generic import ListView, CreateView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/write.html"
    fields = ["title", "text", "author", "visable"]