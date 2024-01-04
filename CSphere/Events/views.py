from django.shortcuts import render, redirect
from .forms import EventApplicationForm
from django.contrib.auth.decorators import login_required
@login_required

def view(request):
    return render(request, 'Events.html')


def view2(request):
    return render(request, 'camping.html')


def event_application(request):
    if request.method == 'POST':
        form = EventApplicationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('success_page')
    else:
        form = EventApplicationForm()

    return render(request, 'events/event_application_form.html', {'form': form})
