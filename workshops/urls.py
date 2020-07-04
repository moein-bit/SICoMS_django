from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkshopListView.as_view(), name='workshops-home'),
    path('workshop/<int:pk>/', views.WorkshopDetailView.as_view(), name='workshop-detail'),
]