from django.contrib import admin
from django.conf import settings
from django.http import JsonResponse
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def root(_request):
    return JsonResponse(
        {
            "name": "ORIUN Backend",
            "status": "ok",
            "health": "/health/",
        }
    )


def health(_request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('', root, name='root'),
    path('health/', health, name='health'),
    path('admin/', admin.site.urls),
    path('call/', include(('call.urls', 'call'), namespace='call')),
    path('student/', include(('student.urls', 'student'), namespace='student')),
    path('person/', include(('person.urls', 'person'), namespace='person')),
    path('employee/', include(('employee.urls', 'employee'), namespace='employee')),
    path('traceability/', include(('traceability.urls', 'traceability'), namespace='traceability')),
    path('application/', include(('application.urls','application'), namespace='application')),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.STORAGE_BACKEND == "local":
    urlpatterns.append(
        re_path(
            r'^local-storage/(?P<path>.*)$',
            serve,
            {'document_root': settings.LOCAL_STORAGE_ROOT},
            name='local_storage',
        )
    )
