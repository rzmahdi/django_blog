from django.contrib import admin
from .models import Blog, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)