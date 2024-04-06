from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Call, University
from .serializers import CallSerializerOpen, CallSerializerClosed

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
        open_calls = Call.objects.filter(active=True)

        if call_id:
            open_calls = open_calls.filter(id=call_id)
        if country:
            open_calls = open_calls.filter(university_id__country=country)
        if language:
            open_calls = open_calls.filter(university_id__language__contains=[language])
        if university_name:
            open_calls = open_calls.filter(university_id__name__icontains=university_name)
        # Serialize the filtered calls using the serializer
        serializer = CallSerializerOpen(open_calls, many=True)
        # Return JSON response
        return JsonResponse(serializer.data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_GET
def closed_calls(request):
    try:
        country = request.GET.get('country')
        language = request.GET.getlist('language')
        name_university = request.GET.get('name_university')
        min_papa_winner = request.GET.get('minimum_papa_winner')
        # Filter calls based on provided criteria (CLOSED CALLS)
        closed_calls = Call.objects.filter(active=False)

        if country:
            closed_calls = closed_calls.filter(university_id__country=country)

        if language:
            closed_calls = closed_calls.filter(university_id__language__overlap=[language])

        if name_university:
            closed_calls = closed_calls.filter(university_id__name__icontains=name_university)

        if min_papa_winner:
            closed_calls = closed_calls.filter(minimum_papa_winner__gte=float(min_papa_winner))

        # Serialize the data
        serializer_closed = CallSerializerClosed(closed_calls, many=True)

        # Return JSON response
        return JsonResponse(serializer_closed.data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)