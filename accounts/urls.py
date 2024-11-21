from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterCreateView.as_view(), name="register"),
]
