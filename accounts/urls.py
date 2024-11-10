from django.urls import path,include
from django.contrib.auth.views import LoginView
from accounts.forms import userLoginForm,UserRegisterForm
from accounts.views import Registerview ,edit_profile
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path ('login/',LoginView.as_view(authentication_form=userLoginForm), name='Login'),
    path ('register/',Registerview.as_view(), name='register'),
    path('profile/',edit_profile, name='profile')
    
    



]