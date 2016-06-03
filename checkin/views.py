from django.utils import timezone
from django.http import HttpResponse, HttpResponseForbidden
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder

import requests
from datetime import datetime
import json
import requests
import mimetypes

from checkin.models import Checkin
from checkin.models import Like
from checkin.models import Place


@csrf_exempt
def create_place(request):
    if not request.method == 'POST':
        return HttpResponse(status=400)

    req = json.loads(request.body.decode('utf-8'))

    for place in req:
        location = place['location']
        if 'state' not in location:
            location['state'] = ''
        if 'country' not in location:
            location['country'] = ''
        if (len(Place.objects.filter(place_id=place['id'])) > 0):
            continue

        new_place = Place(category=place['category'],
            category_list_id=place['category_list'][0]['id'],
            category_list_name=place['category_list'][0]['name'],
            street=location['street'],
            city=location['city'],
            state=location['state'],
            country=location['country'],
            latitude=location['latitude'],
            longitude=location['longitude'],
            place_zip=location['zip'],
            name=place['name'],
            pageUrl=place['pageUrl'],
            place_id=place['id']
        )
        new_place.save()
    return HttpResponse(status=200)


@csrf_exempt
def create(request):
    if not request.method == 'POST':
        return HttpResponse(status=400)

    req = json.loads(request.body.decode('utf-8'))

    for place in req:
        p = Place.objects.get(place_id=place['id'])

        m_date = timezone.make_aware(datetime.strptime(place['visit']['date'], '%Y-%m-%d'), \
                    timezone.get_current_timezone())
        if(len(Checkin.objects.filter(place=p, date=m_date)) == 0):
            Checkin(visit=place['visit']['value'], date=m_date, place=p).save()

        m_date = timezone.make_aware(datetime.strptime(place['like']['date'], '%Y-%m-%d'), \
                    timezone.get_current_timezone())
        if(len(Like.objects.filter(place=p, date=m_date)) == 0):
            Like(like=place['like']['value'], date=m_date, place=p).save()

    return HttpResponse(status=200)

def read(request):
    pass
