from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from lano_end.models import Group

import json

@require_http_methods(['POST'])
@csrf_exempt
def create_group(request):
    obj = json.loads(request.body)
    print('create group obj', obj)
    name = obj['group']['name']
    user_uuid = obj['uuid']
    print('create group name', name)
    print('create group uuid', user_uuid)
    response = {}
    try:
        group = Group(name=name,user_uuid=user_uuid)
        group.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_groups(request):
    obj = json.loads(request.body)
    print('obj', obj)
    user_uuid = obj['uuid']
    response = {}
    try:
        groups = Group.objects.filter(user_uuid__exact=user_uuid).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", groups))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def delete_group(request):
    response = {}
    try:
        if not request.user.is_authenticated:
            group = Group.objects.get(id=request.body)
            group.delete()
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")
