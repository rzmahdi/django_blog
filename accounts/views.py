from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy


class RegisterCreateView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")