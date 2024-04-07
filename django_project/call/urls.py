
from django.urls import path
from .views import CallView, CallDetails, UniversityView


urlpatterns = [
    path('api/', CallView.as_view(), name='call_test'),
    path('api/<int:pk>/', CallDetails.as_view(), name='call_detail'),
    path('university_api/', UniversityView.as_view(), name='univ_test')
]