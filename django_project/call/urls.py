from django.urls import path
from .views import open_calls


urlpatterns = [
    path('open/', open_calls, name='open_calls'),
]