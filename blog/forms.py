from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "comment", "blog")
        widgets = {
            "blog": forms.HiddenInput(),
            "author": forms.HiddenInput(),
        }