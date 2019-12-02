from django.shortcuts import render, redirect
from .forms import SignupInfoForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup(request):
    forms=SignupInfoForm()
    if request.method == 'POST':
        forms=SignupInfoForm(request.POST)
        if forms.is_valid():
            first_name=forms.cleaned_data['first_name']
            last_name=forms.cleaned_data['last_name']
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            password2=forms.cleaned_data['password2']
            email=forms.cleaned_data['email']
            if password == password2:
                User.objects.create_user(first_name=first_name, last_name=last_name,username=username, password=password, email=email)
                n_user = authenticate(request, username=username, password=password)
                if n_user: 
                    login(request, n_user)
                    return redirect('home')                    
                else:
                    print("No user in this name")

    context={'forms':forms}
    return render(request, 'user/signup.html', context)

def login_view(request):
    forms=LoginForm()
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print("First Name: ",request.user.first_name)
        else:
            print("no user")
    context={'forms':forms}
    return render(request, 'user/login.html', context)