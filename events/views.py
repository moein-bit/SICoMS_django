from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Event
from django.urls import reverse_lazy

class EventListView(ListView):
    model = Event
    template_name = 'events/events_home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['-date_posted']

 
class EventDetailView(DetailView):
    model = Event

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'photo', 'summary', 'explanation']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'photo', 'summary', 'explanation']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events-home')

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False
    



