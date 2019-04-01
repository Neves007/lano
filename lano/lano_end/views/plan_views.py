from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from lano_end.models import Plan

import json


@require_http_methods(['POST'])
@csrf_exempt
def create_plan(request):
    obj = json.loads(request.body)
    name = obj['plan']['name']
    area = obj['plan']['area']
    character = obj['plan']['character']
    event = obj['plan']['event']
    exclude = obj['plan']['exclude']
    group_id = obj['plan']['group_id']
    ad_conf = obj['plan']['ad_conf']
    user_uuid = obj['uuid']
    response = {}
    try:
        plan = Plan(name=name, area=area, character=character, event=event, exclude=exclude, group_id=group_id,
                    ad_conf=ad_conf, user_uuid=user_uuid)
        plan.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['GET'])
@csrf_exempt
def get_plans(request):
    response = {}
    try:
        plans = Plan.objects.all().order_by('id')
        response['list'] = json.loads(serializers.serialize("json", plans))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def update_plans(request):
    obj = json.loads(request.body)
    name = obj['fields']['name']
    area = obj['fields']['area']
    character = obj['fields']['character']
    event = obj['fields']['event']
    exclude = obj['fields']['exclude']
    group_id = obj['fields']['group_id']
    ad_conf = obj['fields']['ad_conf']
    response = {}
    try:
        # plan = Plan(name=name, area=area, character=character, event=event, exclude=exclude, group_id=group_id,
        #             ad_conf=ad_conf)
        plan = Plan.objects.get(id=obj['pk'])
        plan.name = name
        plan.area = area
        plan.character = character
        plan.event = event
        plan.exclude = exclude
        plan.group_id = group_id
        plan.ad_conf = ad_conf
        plan.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def delete_plan(request):
    response = {}
    try:
        if not request.user.is_authenticated:
            plan = Plan.objects.get(id=request.body)
            plan.delete()
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")

