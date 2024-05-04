from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('call/', include(('call.urls', 'call'), namespace='call')),
    path('student/', include(('student.urls', 'student'), namespace='student')),
    path('person/', include(('person.urls', 'person'), namespace='person')),
    path('application/', include('application.urls')),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
