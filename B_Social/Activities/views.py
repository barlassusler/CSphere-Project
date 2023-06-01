from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view(request):
    return render(request,'Activities.html')
def view1(request):
    return render(request, 'progress.html')