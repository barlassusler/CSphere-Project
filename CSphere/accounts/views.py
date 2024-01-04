from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home_login')
    else:
        form = SignInForm()
    return render(request, 'login.html', {'form': form})


def home_login(request):
    return render(request, 'home_login.html')