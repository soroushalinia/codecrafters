from django import forms
from .models import CommentBlogtModel

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = CommentBlogtModel
        exclude = ('public', 'created', 'blog', 'parent')