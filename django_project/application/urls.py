from . import views
from django.urls import path


urlpatterns = [
    path('region_call/', views.get_region_call, name='region_call'),
    path('create_forms/', views.create_forms, name='create_forms'),
    path('download/', views.download_file, name='download_file'),
    path('upload/', views.upload_file, name='upload_file'),
    path('submit/', views.submit_application, name='submit_application'),
    path('student/', views.ApplicationsStudent.as_view(), name='student_applications'),
    path('comments/', views.ApplicationComments.as_view(), name='application_comments'),
    path('edit/', views.edit_application, name='edit_application'),
    path('applicants/<int:call_id>/', views.applicants, name='applicants'),
]
