from django.urls import path
from .views import post_verif_code
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('code/', post_verif_code.as_view(), name='request_verif_code'),
]
