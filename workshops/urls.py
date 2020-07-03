from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkshopListView.as_view(), name='workshops-home'),
]