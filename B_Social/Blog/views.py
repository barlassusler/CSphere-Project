from django.shortcuts import render

# Create your views here.
def progress(request):
    return render(request, 'blog.html')