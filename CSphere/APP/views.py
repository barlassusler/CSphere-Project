from django.shortcuts import render,redirect

def index(request):
    return render(request,'base.html')
def home(request):
    return render(request, 'home.html')
def login_view(request):

    if user_logged_in_successfully:
        return redirect('home')
    else:

        return render(request, 'login.html', {'error_message': 'Invalid credentials'})