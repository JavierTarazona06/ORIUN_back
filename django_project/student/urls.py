from django.urls import path
from .views import ApplicationDataView

urlpatterns = [
    path('info_application/', ApplicationDataView.as_view(), name='application_data'),
]
