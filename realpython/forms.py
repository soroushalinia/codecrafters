from django import forms
from realpython.models import RealPythonCommentTopicModel, RealpythonDescribeTopicModel
from ckeditor.widgets import CKEditorWidget


class TopicCommentForm(forms.ModelForm):
    class Meta:
        model = RealPythonCommentTopicModel
        exclude = ('describetapic', 'parent', 'public', 'created')



class DescribeTopicModelForm(forms.ModelForm):
    class Meta:
        model = RealpythonDescribeTopicModel
        fields = '__all__'  # Include all fields from the model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripStion'].widget = CKEditorWidget()  # Use CKEditor for the 'describtion' field
