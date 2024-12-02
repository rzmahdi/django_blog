from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog, admin.ModelAdmin)
admin.site.register(Comment)