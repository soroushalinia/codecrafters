from django import forms
from .models import ConnectModel

class ConnectForm(forms.ModelForm):
    class Meta:
        model = ConnectModel
        exclude = ('read',)