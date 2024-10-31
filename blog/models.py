from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    visable = models.BooleanField(default=True)

    def __str__(self):
        return self.title