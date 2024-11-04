from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from django.shortcuts import render
from . import models, forms
# Create your views here.
class projectlistview(ListView):
    model = models.projects
    template_name = 'projects/list.html'
#_______________________________________________________________________
class projectCreateview(CreateView):
    model = models.projects
    form_class = forms.Projectcreateform
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')

