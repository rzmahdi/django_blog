from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.all().order_by('-creation_time')
    


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


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/delete.html"
    success_url = reverse_lazy("blogs")