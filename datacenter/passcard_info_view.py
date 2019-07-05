from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render


def is_visit_long(time, limit):
    minutes = time.seconds // 60
    return minutes > limit    


def passcard_info_view(request, passcode):
    limit = 60
    this_passcard_visits = []
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": format_duration(visit.get_duration()),
                "is_strange": is_visit_long(visit.get_duration(), limit)
            },
        )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
