from django.urls import path
from .views import open_calls,closed_calls


urlpatterns = [
    path('open/', open_calls, name='open_calls'),
    path('closed/', closed_calls, name='closed_calls'),

]