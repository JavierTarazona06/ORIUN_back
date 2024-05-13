from django.urls import path
from .views import PostUserEmployee, ReadUserEmployee, DeleteUserEmployee
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('post/', PostUserEmployee.as_view(), name='post_user_employee'),
    path('get/<int:pk>/', ReadUserEmployee.as_view(), name='read_user_employee'),
    path('delete/<int:pk>/', DeleteUserEmployee.as_view(), name='delete_user_employee')
]