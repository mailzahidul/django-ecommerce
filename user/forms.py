from django import forms
from .models import SignupInfo

class SignupInfoForm(forms.ModelForm):
    password2=forms.CharField(label="Confirm Password")
    class Meta:
        model = SignupInfo
        fields = ('first_name','last_name','email','username','password','password2')
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