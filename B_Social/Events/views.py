from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view(request):
    return render(request, 'Events.html')

def view2(request):
    return render(request,'camping.html')