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
    path('documents/<int:call_id>/<int:student_id>/', views.documents, name='documents_student'),
    path('modify/<int:call_id>/<int:student_id>/',views.modify ,name= 'modify_application'),
    path('accept-documents/<int:student_id>/<int:call_id>/',views.accept_documents,  name='accept_documents'),
    path('student-info/<int:call_id>/<int:student_id>/', views.get_student_info, name= 'student_info')

]
