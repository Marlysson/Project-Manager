from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    ''' Cadastro de User '''

    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')


class UserLoginForm(forms.ModelForm):
    ''' Cadastro de User '''

    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'password')
