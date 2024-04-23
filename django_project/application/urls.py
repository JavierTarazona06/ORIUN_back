from . import views
from django.urls import path


urlpatterns = [
    path('region_call/', views.get_region_call, name='region_call'),
    path('create_forms/', views.create_forms, name='create_forms'),
    path('download/', views.download_file, name='download_file'),
    path('upload/', views.upload_file, name='upload_file'),
]
