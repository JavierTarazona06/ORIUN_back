from django.urls import path
from .views import ApplicationDataView, EligibilityView

urlpatterns = [
    path('elegible/', EligibilityView.as_view(), name='eligibility'),
    path('info_application/', ApplicationDataView.as_view(), name='application_data'),
]
