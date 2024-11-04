from django import forms
from . import models


class Projectcreateform(forms.ModelForm):
    class Meta:
        model  = models.projects
        fields = ['category' ,'title', 'description']
        widgets ={
            'category' : forms.Select(),
            'title' : forms.TextInput(),
            'description' : forms.Textarea(),
        }
