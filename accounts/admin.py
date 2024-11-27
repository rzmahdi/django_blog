from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    add_form = forms.SingUpForm
    form = forms.LoginForm

admin.site.register(CustomUserModel, CustomUserAdmin)