from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    add_form = forms.SignUpForm
    form = forms.LoginForm
    list_display = ["username", "email", "is_staff"]
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("birth_date", )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email", "birth_date")}),
    )

admin.site.register(CustomUserModel, CustomUserAdmin)