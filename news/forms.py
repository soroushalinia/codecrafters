from django import forms
from .models import NewsCommentModel

class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsCommentModel
        exclude = ('public', 'created', 'news', 'parent')