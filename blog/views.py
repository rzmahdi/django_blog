from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.all().order_by('-creation_time')
    

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog/write.html"
    fields = ["title", "text", "visable"]
    success_url = reverse_lazy("blogs")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = "blog/edit.html"
    fields = ["title", "text", "visable"]
    success_url = reverse_lazy("blogs")

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = "blog/delete.html"
    success_url = reverse_lazy("blogs")

    def test_func(self):
        blog = self.get_object()
        return blog.author == self.request.user