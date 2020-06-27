from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.

def home(request):
    context = {
        'events': Event.objects.all(),
        'title': "Events"
    }
    return render(request, 'events/events_home.html', context)