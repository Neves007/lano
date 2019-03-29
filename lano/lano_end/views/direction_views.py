from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# from lano_end.models import Group

import json


@require_http_methods(['POST'])
@csrf_exempt
def monitor_web_add(request):
    obj = json.loads(request.body)
    print('ooooooooooooooooooooooooobj', obj)

    response = {}
    try:
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")
