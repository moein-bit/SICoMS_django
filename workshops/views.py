from django.shortcuts import render
from django.views.generic import ListView
from .models import Workshop

class WorkshopListView(ListView):
    model = Workshop
    context_object_name = 'workshops'
    ordering = ['-date_posted']
    paginate_by = 2