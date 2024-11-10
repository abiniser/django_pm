from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
#AuthenticationForm is for make sure that the user is login
#UserCreationForm is form create a user
#UserChangeForm is for create the user profile

attrs = {'class': 'form-control'}


class userLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(userLoginForm,self).__init__( *args, **kwargs)
    username = forms.CharField(
       label='Username' ,
       widget=forms.TextInput(attrs=attrs)
    )
    Password = forms.CharField(
       label='Password' ,
       widget=forms.PasswordInput(attrs=attrs)
    )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class UserRegisterForm(UserCreationForm):
      first_name = forms.CharField(
       label='First Name' ,
       widget=forms.TextInput(attrs=attrs)
       )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      last_name = forms.CharField(
      label='Last Name' ,
      widget=forms.TextInput(attrs=attrs)
    )
#_______________________________________________________________      
      username = forms.CharField(
       label='Username' ,
       widget=forms.TextInput(attrs=attrs)
      )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      email = forms.EmailField(
       label='Email' ,
       widget=forms.TextInput(attrs=attrs)
      )
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%      
      password1 = forms.CharField(
      label='Password' ,
      strip=False,
      widget=forms.PasswordInput(attrs=attrs)
      )
      password2 = forms.CharField(
      label='Password Confirmation' ,
      strip=False,
      widget=forms.PasswordInput(attrs=attrs)
      )
      class Meta(UserCreationForm):
            fields=(' first_name','last_name','username', 'email' )    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class ProfileForm(UserChangeForm):
     password =None
     class Meta:
          model = User
          fields =['first_name','last_name','email']
          widgets ={
               'first_name': forms.TextInput(attrs=attrs),
               'list_name': forms.TextInput(attrs=attrs),
               'email': forms.EmailInput(attrs=attrs),
          }