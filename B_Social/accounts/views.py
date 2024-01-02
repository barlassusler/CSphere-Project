from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Kullanıcı başarıyla kayıt oldu, şimdi login sayfasına yönlendir
                return redirect('login')  # 'login' yerine kendi login sayfanızın adını kullanın
            else:
                # Kullanıcı doğrulanamadı, isteğe bağlı olarak bir hata mesajı verebilirsiniz.
                return render(request, 'signup.html', {'form': form, 'error_message': 'Kullanıcı doğrulanamadı'})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'login.html', {'form': form})
