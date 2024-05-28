from django.urls import path
from rest_framework.documentation import include_docs_urls
from .views import (
    OpenCallsStudent, ClosedCallsStudent, CallView, CallDetails, OpenCalls, ClosedCalls,
    CallsFilterSearch, OpenCallDetailStudent, ClosedCallDetailStudent, UniversityDetails,
    UniversityView, UpdateCallsView, UpdateUniversityView, SetClosed, SetOpen, statistics
)


urlpatterns = [
    path('open/', OpenCallsStudent.as_view(), name='open_calls'),
    path('closed/', ClosedCallsStudent.as_view(), name='closed_calls'),
    path('api/', CallView.as_view(), name='calls_list'),
    path('api/<int:pk>/', CallDetails.as_view(), name='calls_detail'),
    path('api_put/<int:pk>/', UpdateCallsView.as_view(), name='calls_update_by_id'),
    path('api/opened/', OpenCalls.as_view(), name='calls_opened'),
    path('api/closed/', ClosedCalls.as_view(), name='calls_closed'),
    path('api/employee_filter/', CallsFilterSearch.as_view(), name='calls_employee_filter'),
    path('university_api/', UniversityView.as_view(), name='univ_list'),
    path('university_api/<int:pk>/', UniversityDetails.as_view(), name='univ_detail'),
    path('university_api_put/<int:pk>/', UpdateUniversityView.as_view(), name='University_update_by_id'),
    path('open/<int:id>/', OpenCallDetailStudent.as_view(), name='open-call-detail'),
    path('closed/<int:id>/', ClosedCallDetailStudent.as_view(), name='closed-call-detail'),
    path('set_closed/', SetClosed.as_view(), name='set_call_closed'),
    path('set_open/', SetOpen.as_view(), name='set_call_open'),
    path("docs/", include_docs_urls(title="CALLS docs")),
    path("statistics/", statistics, name="statistics"),
]
