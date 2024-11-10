from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# LoginRequiredMixin is to stop none register user from useing the projects management
# Create your views here.
class projectlistview( LoginRequiredMixin, ListView):
    model = models.projects
    template_name = 'project/list.html'
    paginate_by=6
    def get_queryset(self):
        query_set = super().get_queryset() 
        where = {'user_id': self.request.user}
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
    #this def is for adding the projcet user  into the project information by sutk up the id number of the user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
#______________________________________________________________________________
class projectUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView ):
    model = models.projects
    form_class = forms.ProjectUpdateform
    template_name = 'project/update.html'
    # this fun is for forbdnn the none user form edit the project
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
   # success_url = reverse_lazy('project_list')
   #this for stay on the same page after the update
    def get_success_url(self):
        return reverse('project_Update',args = [self.object.id])
#_____________________________________________________________________________________________________
class ProjectDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView ):
    model = models.projects
    template_name = 'project/delete.html '
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().user_id == self.request.user.id
#________________________________________________________________________________
class TaskCreateview(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = models.task
    fields= ['project', 'description']
    #this is for to give Error if someone try to ask for the t TaskCreate on the browse
    http_method_names =['post']
    def test_func(self):
        #this for get the id project 
        project_id = self.request.POST.get('project','')
        #this to coper the projet id 
        return models.project.object.get(pk = project_id).user_id== self.request.user.id
    def get_success_url(self):
        return reverse( 'project_update',args = [self.object.project.id])
#__________________________________________________________________________________
class TaskUpdateview(LoginRequiredMixin,UserPassesTestMixin, UpdateView ):
    model = models.task
    fields= ['is_completed']
    #this is for to give Error if someone try to ask for the t TaskCreate on the browse
    http_method_names =['post']
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    def get_success_url(self):
        return reverse('project_Update',args = [self.object.project.id])
#_____________________________________________________________________________________
#THIS for delete the task
class TaskDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.task
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    def get_success_url(self):
        return reverse('project_Update',args = [self.object.project.id])

