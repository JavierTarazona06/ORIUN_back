from . import views
from django.urls import path

from .views import OrderDocs, OrderPAPA, OrderAdvance, OrderLanguage, OrderPBM, OrderGeneral, SetWinner, RemoveWinner, GetAllApplications, PreAssignWinners

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
    path('accept-documents/<int:call_id>/<int:student_id>/',views.accept_documents,  name='accept_documents'),
    path('student-info/<int:call_id>/<int:student_id>/', views.get_student_info, name= 'student_info'),
    path('get-state/<int:call_id>/<int:student_id>/', views.get_state, name='get_state'),
    path('add-comment/<int:call_id>/<int:student_id>/', views.add_comment, name='comment_application'),
    path('order_docs/<int:pk>/', OrderDocs.as_view(), name='order_apps_by_docs'),
    path('order_papa/<int:pk>/', OrderPAPA.as_view(), name='order_apps_by_papa'),
    path('order_adva/<int:pk>/', OrderAdvance.as_view(), name='order_apps_by_advance'),
    path('order_lang/<int:pk>/', OrderLanguage.as_view(), name='order_apps_by_language'),
    path('order_pbm/<int:pk>/', OrderPBM.as_view(), name='order_apps_by_pbm'),
    path('order/<int:pk>/', OrderGeneral.as_view(), name='order_apps_general'),
    path('get_all/<int:pk>/', GetAllApplications.as_view(), name='all_apps_general_by_call_id'),
    path('winner/', SetWinner.as_view(), name='set_winner'),
    path('not_winner/', RemoveWinner.as_view(), name='not_winner'),
    path('pre_assign_winners/<int:pk>/', PreAssignWinners.as_view(), name='pre_assign_winners')
]
