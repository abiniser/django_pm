from django import forms
from . import models

attrs = {'class':'form-control'}
class Projectcreateform(forms.ModelForm):
    class Meta:
        model  = models.projects
        fields = ['category' ,'title', 'description']
        widgets ={
            'category' : forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'description' : forms.Textarea(attrs=attrs),
        }

#__________________________________________________________________
class ProjectUpdateform(forms.ModelForm):
    class Meta:
        model  = models.projects
        fields = ['category' ,'title', 'description']
        widgets ={
            'category' : forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }
        
