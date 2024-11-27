from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel


class SingUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('email', 'birth_date')


class LoginForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        # fields = ('username', 'email', 'birth_date')