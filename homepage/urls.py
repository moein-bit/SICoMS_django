from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage-home"),
    path('about/', views.about, name="about-page")
]