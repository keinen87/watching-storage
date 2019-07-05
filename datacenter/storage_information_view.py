from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from datacenter.passcard_info_view import is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    limit = 60 
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": format_duration(visit.get_duration()),
                "is_strange": is_visit_long(visit.get_duration(), limit)
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
