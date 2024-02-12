from django import forms
from .models import CommentTopicModel


class TopicCommentForm(forms.ModelForm):
    class Meta:
        model = CommentTopicModel
        exclude = ('describetapic', 'parent', 'public', 'created')