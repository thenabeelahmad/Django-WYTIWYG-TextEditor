from django import forms
from django.forms import widgets
from .models import BasicForm

class BasicF(forms.ModelForm):
    class Meta:
        model = BasicForm
        fields = [
            'title',
            'username',
            'realtext'

        ]
    
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Your titile goes here'}),
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your username goes here'}),
            'realtext' : forms.Textarea(attrs={'class':'form-control',})

        }