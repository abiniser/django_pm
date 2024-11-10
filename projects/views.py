from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
# LoginRequiredMixin is to stop none register user from useing the projects management
# Create your views here.
class projectlistview( LoginRequiredMixin, ListView):
    model = models.projects
    template_name = 'project/list.html'
    paginate_by=6
    def get_queryset(self):
        query_set = super().get_queryset() 
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)
#__________________________________________________________
class projectCreateview(LoginRequiredMixin,CreateView):
    model = models.projects
    form_class = forms.Projectcreateform
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')
#______________________________________________________________________________
class projectUpdateview(LoginRequiredMixin,UpdateView ):
    model = models.projects
    form_class = forms.ProjectUpdateform
    template_name = 'project/update.html'
   # success_url = reverse_lazy('project_list')
   #this for stay on the same page after the update
    def get_success_url(self):
        return reverse('project_Update',args = [self.object.id])
#_____________________________________________________________________________________________________
class ProjectDeleteview(LoginRequiredMixin,DeleteView ):
    model = models.projects
    template_name = 'project/delete.html '
    success_url = reverse_lazy('project_list')
#________________________________________________________________________________
class TaskCreateview(LoginRequiredMixin, CreateView):
    model = models.task
    fields= ['project', 'description']
    #this is for to give Error if someone try to ask for the t TaskCreate on the browse
    http_method_names =['post']
    def get_success_url(self):
        return reverse( 'project_update',args = [self.object.project.id])
#__________________________________________________________________________________
class TaskUpdateview(LoginRequiredMixin, UpdateView ):
    model = models.task
    fields= ['is_completed']
    #this is for to give Error if someone try to ask for the t TaskCreate on the browse
    http_method_names =['post']
    def get_success_url(self):
        return reverse('project_Update',args = [self.object.project.id])
#_____________________________________________________________________________________
#THIS for delete the task
class TaskDeleteview(LoginRequiredMixin,DeleteView):
    model = models.task
    def get_success_url(self):
        return reverse('project_Update',args = [self.object.project.id])

