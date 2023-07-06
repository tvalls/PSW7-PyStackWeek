from django.urls import re_path
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
]