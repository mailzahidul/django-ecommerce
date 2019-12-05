from django import forms
from .models import SignupInfo

class SignupInfoForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    username=forms.CharField()
    password1=forms.CharField(label="Password")
    password2=forms.CharField(label="Confirm Password")
        # widgets= {
        #     'first_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control'}),
        #     'username':forms.TextInput(attrs={'class':'form-control'}),
        #     'password':forms.PasswordInput(attrs={'class':'form-control'}),
        #     'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        # }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))