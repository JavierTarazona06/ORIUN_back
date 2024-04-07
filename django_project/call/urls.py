from django.urls import path
from .views import OpenCalls,ClosedCalls


urlpatterns = [
    path('open/', OpenCalls.as_view(), name='open_calls'),
    path('closed/', ClosedCalls.as_view(), name='closed_calls'),

]