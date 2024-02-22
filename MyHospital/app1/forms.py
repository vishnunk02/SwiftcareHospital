from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username' , "class" : "form-control" , "id" : "name"}),
        label=''
    )
    
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password' , "class" : "form-control" , "id" : "pass"}),
        label=''
    )
    
    
class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name',"class":"form-control mb-3"}),
        label=''
    )
    username = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={'placeholder': 'Username',"class":"form-control mb-3"}),
        label=''
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',"class":"form-control mb-3"}),
        label=''
    )
    
class PatientForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
        label=''
    )
    username = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label=''
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label=''
    )