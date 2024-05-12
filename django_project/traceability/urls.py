from django.urls import path
from .views import GetTraceability
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('get/', GetTraceability.as_view(), name='get_trace'),
    path("docs/", include_docs_urls(title="Student docs"))
]
