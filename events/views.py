from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Moein',
        'title': 'Post 1',
        'content': 'First opportunity to go abroad!',
        'date_posted': 'June 25, 2020'
    },
    {
        'author': 'Hnaye',
        'title': 'Post 2',
        'content': 'Second opportunity to go abroad!',
        'date_posted': 'June 26, 2020'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': "Events"
    }
    return render(request, 'events/events_home.html', context)