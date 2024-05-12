from datetime import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.http import JsonResponse

from .models import Traceability
from .serializers import TraceabilitySerializer

from employee.permissions import IsEmployee

class GetTraceability(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request):
        try:

            id = request.GET.get('id')
            view = request.GET.get('view')
            method = request.GET.get('method')
            user_id = request.GET.get('user_id')
            from_date = request.GET.get('from_date')
            until_date = request.GET.get('until_date')

            qset = Traceability.objects.all()
            if id:
                qset = qset.filter(id=id)
            if view:
                qset = qset.filter(view=view)
            if method:
                qset = qset.filter(method=method)
            if user_id:
                qset = qset.filter(user_id=user_id)
            if from_date:
                qset = qset.filter(time__gte=from_date)
            if until_date:
                qset = qset.filter(time__lte=until_date)

            qset_r = TraceabilitySerializer(qset, many=True).data

            return JsonResponse(qset_r, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
