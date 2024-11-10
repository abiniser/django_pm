from django.views.generic import CreateView
from django.shortcuts import redirect, render
from accounts.forms import ProfileForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
class Registerview(CreateView):
    form_class= UserRegisterForm
    #success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('project_list')
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@login_required
def edit_profile(request):
    if request.method=='POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:    
        form = ProfileForm(instance=request.user)
        return render(request, 'profile.html',{
            'form': form
        })