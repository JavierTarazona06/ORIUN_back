from django.urls import path
from .views import create_forms, get_region_call


urlpatterns = [
    path('region_call/', get_region_call, name='region_call'),
    path('create_forms/', create_forms, name='create_forms'),
]
