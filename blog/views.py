from django.views.generic import ListView, CreateView, UpdateView
from .models import Blog
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/write.html"
    fields = ["title", "text", "author", "visable"]
    success_url = reverse_lazy("blogs")


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/edit.html"
    fields = ["title", "text", "visable"]
    success_url = reverse_lazy("blogs")