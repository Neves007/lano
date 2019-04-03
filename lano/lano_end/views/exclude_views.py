from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from bs4 import BeautifulSoup
import requests

from lano_end.models import Exclude_web
from lano_end.models import Exclude_weibo
from lano_end.models import Exclude_wechat

import json


@require_http_methods(['POST'])
@csrf_exempt
def exclude_web_add(request):
    obj = json.loads(request.body)
    # print('obj', obj)
    # name = obj['name']
    domain = obj['domain']
    plan_id = obj['planid']
    # print('plan_id', plan_id)
    res = requests.get(domain)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml').title.text
    # print('soup ', soup)
    name = soup
    status = 1
    response = {}
    try:
        exclude_web = Exclude_web(name=name, domain=domain, status=status, plan_id=plan_id)
        exclude_web.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_exclude_web(request):
    obj = json.loads(request.body)
    plan_id = obj['planid']
    print('plan_id', plan_id)
    response = {}
    try:
        exclude_web = Exclude_web.objects.filter(plan_id=plan_id).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", exclude_web))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def exclude_web_delete(request):
    response = {}
    try:
        exclude_web = Exclude_web.objects.get(id=request.body)
        exclude_web.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_exclude_weibo(request):
    obj = json.loads(request.body)
    plan_id = obj['planid']
    response = {}
    try:
        exclude_weibo = Exclude_weibo.objects.filter(plan_id=plan_id).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", exclude_weibo))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def exclude_weibo_add(request):
    obj = json.loads(request.body)
    # print('obj', obj)
    name = obj['name']
    uid = '12345'
    status = 1
    plan_id = obj['planid']
    response = {}
    try:
        exclude_weibo = Exclude_weibo(name=name, uid=uid, status=status, plan_id=plan_id)
        exclude_weibo.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def exclude_weibo_delete(request):
    response = {}
    try:
        exclude_weibo = Exclude_weibo.objects.get(id=request.body)
        exclude_weibo.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_exclude_wechat(request):
    obj = json.loads(request.body)
    plan_id = obj['planid']
    response = {}
    try:
        exclude_wechat = Exclude_wechat.objects.filter(plan_id=plan_id).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", exclude_wechat))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def exclude_wechat_add(request):
    obj = json.loads(request.body)
    # print('obj', obj)
    name = obj['name']
    wxid = 'weixinid'
    status = 1
    plan_id = obj['planid']
    response = {}
    try:
        exclude_wechat = Exclude_wechat(name=name, wxid=wxid, status=status, plan_id=plan_id)
        exclude_wechat.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def exclude_wechat_delete(request):
    response = {}
    try:
        exclude_wechat = Exclude_wechat.objects.get(id=request.body)
        exclude_wechat.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")
