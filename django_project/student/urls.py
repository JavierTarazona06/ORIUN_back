# my_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.offer_list, name='student-view'),
]
