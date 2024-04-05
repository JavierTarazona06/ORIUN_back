from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Call, University
from .serializers import CallSerializer


@require_GET
def open_calls(request):
    try:
        call_id = request.GET.get('id')
        country = request.GET.get('country')
        language = request.GET.get('language')
        university_name = request.GET.get('name_university')


        if university_name:
            university_name = university_name.lower()

        # Filter open calls based on provided criteria (OPEN CALLS)
        open_calls_queryset = Call.objects.filter(active=True)

        if call_id:
            open_calls_queryset = open_calls_queryset.filter(id=call_id)
        if country:
            open_calls_queryset = open_calls_queryset.filter(university_id__country=country)
        if language:
            open_calls_queryset = open_calls_queryset.filter(university_id__language__contains=[language])
        if university_name:

            open_calls_queryset = open_calls_queryset.filter(university_id__name__icontains=university_name)

        # Serialize the filtered calls using the serializer
        serializer = CallSerializer(open_calls_queryset, many=True)

        # Return JSON response
        return JsonResponse(serializer.data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
