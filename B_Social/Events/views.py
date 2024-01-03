from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventApplicationForm

# Create your views here.
def view(request):
    return render(request, 'Events.html')

def view2(request):
    return render(request,'progress.html')

def event_application(request):
    if request.method == 'POST':
        form = EventApplicationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('success_page')
    else:
        form = EventApplicationForm()

    return render(request, 'events/event_application_form.html', {'form': form})