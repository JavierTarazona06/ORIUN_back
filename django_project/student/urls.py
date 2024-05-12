from django.urls import path
from .views import ApplicationDataView, EligibilityView
from .views import post_user_student, ReadUserStudent, DeleteUserStudent
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('eligible/', EligibilityView.as_view(), name='eligibility'),
    path('info_application/', ApplicationDataView.as_view(), name='application_data'),
    path('post/', post_user_student.as_view(), name='post_user_student'),
    path('get/<int:pk>/', ReadUserStudent.as_view(), name='read_user_student'),
    path('delete/<int:pk>/', DeleteUserStudent.as_view(), name='delete_user_student'),
    path("docs/", include_docs_urls(title="Student docs"))
]
