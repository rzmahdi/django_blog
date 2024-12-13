from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.urls import reverse


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.all().order_by('-creation_time')
    

class BlogDetailView(FormMixin, DetailView):
    model = Blog
    template_name = "blog/detail.html"
    context_object_name = "blog"
    form_class = CommentForm


    def get_success_url(self):
        return reverse("detail_blog", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentForm(initial={"blog": self.object, "author": self.request.user})
        return context
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass

    def form_valid(self, form):
        form.save()
        return super(BlogDetailView, self).form_valid(form)


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