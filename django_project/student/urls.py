from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.OfferList.as_view(), name='student-view'),
    path('offers/<int:pk>/', views.OfferDetails.as_view(), name='offer_detail'),
]
