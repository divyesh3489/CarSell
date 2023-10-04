from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Registration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        
