from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)