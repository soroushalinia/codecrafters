from django import forms
from .models import CommentTopicModel, DescribeTopicModel
from ckeditor.widgets import CKEditorWidget


class TopicCommentForm(forms.ModelForm):
    class Meta:
        model = CommentTopicModel
        exclude = ('describetapic', 'parent', 'public', 'created')



class DescribeTopicModelForm(forms.ModelForm):
    class Meta:
        model = DescribeTopicModel
        fields = '__all__'  # Include all fields from the model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['describtion'].widget = CKEditorWidget()  # Use CKEditor for the 'describtion' field
