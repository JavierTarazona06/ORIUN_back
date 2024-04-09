from django.urls import path
from .views import OpenCallsStudent, ClosedCallsStudent, CallView, CallDetails, OpenCalls, ClosedCalls, CallsFilterSearch, OpenCallDetailStudent, ClosedCallDetailStudent, UniversityDetails
from .views import UniversityView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('open/', OpenCallsStudent.as_view(), name='open_calls'),
    path('closed/', ClosedCallsStudent.as_view(), name='closed_calls'),
    path('api/', CallView.as_view(), name='calls_list'),
    path('api/<int:pk>/', CallDetails.as_view(), name='calls_detail'),
    path('api/opened/', OpenCalls.as_view(), name='calls_opened'),
    path('api/closed/', ClosedCalls.as_view(), name='calls_closed'),
    path('api/employee_filter/', CallsFilterSearch.as_view(), name='calls_employee_filter'),
    path('university_api/', UniversityView.as_view(), name='univ_list'),
    path('university_api/<int:pk>/', UniversityDetails.as_view(), name='calls_detail'),
    path('open/<int:id>/', OpenCallDetailStudent.as_view(), name='open-call-detail'),
    path('closed/<int:id>/', ClosedCallDetailStudent.as_view(), name='closed-call-detail'),
    path("docs/", include_docs_urls(title="CALLS docs"))
]