from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Student listeleme sayfanızın adını buraya ekleyin
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('student_list')  # Student listeleme sayfanızın adını buraya ekleyin
    else:
        form = CustomAuthenticationForm()

    return render(request, 'user_login.html', {'form': form})



