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
def create_ad_plan(request):
    obj = json.loads(request.body)
    ad_name = obj['plan']['ad_name']
    ad_match = obj['plan']['ad_match']
    ad_exclude = obj['plan']['ad_exclude']
    group_id = obj['plan']['group_id']
    user_uuid = obj['uuid']
    response = {}
    try:
        plan = Plan(fast_name=None, fast_area=None, fast_character=None, fast_event=None, fast_exclude=None,
                    ad_name=ad_name,ad_match=ad_match,ad_exclude=ad_exclude, group_id=group_id, user_uuid=user_uuid)
        plan.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def create_fast_plan(request):
    obj = json.loads(request.body)
    fast_name = obj['plan']['fast_name']
    fast_area = obj['plan']['fast_area']
    fast_character = obj['plan']['fast_character']
    fast_event = obj['plan']['fast_event']
    fast_exclude = obj['plan']['fast_exclude']
    group_id = obj['plan']['group_id']
    user_uuid = obj['uuid']
    response = {}
    try:
        plan = Plan(fast_name=fast_name, fast_area=fast_area, fast_character=fast_character, fast_event=fast_event,fast_exclude=fast_exclude,
                    ad_name=None,ad_match=None,ad_exclude=None, group_id=group_id, user_uuid=user_uuid)
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
def update_ad_plans(request):
    obj = json.loads(request.body)
    ad_name = obj['fields']['ad_name']
    ad_match = obj['fields']['ad_match']
    ad_exclude = obj['fields']['ad_exclude']
    group_id = obj['fields']['group_id']
    response = {}
    try:
        # plan = Plan(ad_name=name, area=area, character=character, event=event, exclude=exclude, group_id=group_id,
        #             ad_conf=ad_conf)
        plan = Plan.objects.get(id=obj['pk'])
        plan.ad_name = ad_name
        plan.ad_match = ad_match
        plan.ad_exclude = ad_exclude
        plan.fast_name = None
        plan.fast_area = None
        plan.fast_character = None
        plan.fast_event = None
        plan.fast_exclude = None
        plan.group_id = group_id
        plan.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def update_fast_plans(request):
    obj = json.loads(request.body)
    fast_name = obj['fields']['fast_name']
    fast_area = obj['fields']['fast_area']
    fast_character = obj['fields']['fast_character']
    fast_event = obj['fields']['fast_event']
    fast_exclude = obj['fields']['fast_exclude']
    group_id = obj['fields']['group_id']
    response = {}
    try:
        # plan = Plan(ad_name=name, area=area, character=character, event=event, exclude=exclude, group_id=group_id,
        #             ad_conf=ad_conf)
        plan = Plan.objects.get(id=obj['pk'])
        plan.ad_name = None
        plan.ad_match = None
        plan.ad_exclude = None
        plan.fast_name = fast_name
        plan.fast_area = fast_area
        plan.fast_character = fast_character
        plan.fast_event = fast_event
        plan.fast_exclude = fast_exclude
        plan.group_id = group_id
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



