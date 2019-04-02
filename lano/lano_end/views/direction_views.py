from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from bs4 import BeautifulSoup
import requests

from lano_end.models import Monitor_web
from lano_end.models import Monitor_weibo
from lano_end.models import Monitor_wechat

import json


@require_http_methods(['POST'])
@csrf_exempt
def monitor_web_add(request):
    obj = json.loads(request.body)
    print('obj', obj)
    # name = obj['name']
    domain = obj['domain']
    plan_id = obj['planid']
    # print('plan_id', plan_id)
    res = requests.get(domain)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml').title.text
    print('soup ', soup)
    name = soup
    status = 1
    response = {}
    try:
        monitor_web = Monitor_web(name=name, domain=domain, status=status, plan_id=plan_id)
        monitor_web.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_monitor_web(request):
    obj = json.loads(request.body)
    plan_id = obj['planid']
    # print('plan_id', plan_id)
    response = {}
    try:
        monitor_web = Monitor_web.objects.filter(plan_id=plan_id).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", monitor_web))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def monitor_web_delete(request):
    response = {}
    try:
        monitor_web = Monitor_web.objects.get(id=request.body)
        monitor_web.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_monitor_weibo(request):
    obj = json.loads(request.body)
    plan_id = obj['planid']
    response = {}
    try:
        monitor_weibo = Monitor_weibo.objects.filter(plan_id=plan_id).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", monitor_weibo))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def monitor_weibo_add(request):
    obj = json.loads(request.body)
    # print('obj', obj)
    name = obj['name']
    uid = '12345'
    status = 1
    plan_id = obj['planid']
    response = {}
    try:
        monitor_weibo = Monitor_weibo(name=name, uid=uid, status=status, plan_id=plan_id)
        monitor_weibo.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def monitor_weibo_delete(request):
    response = {}
    try:
        monitor_weibo = Monitor_weibo.objects.get(id=request.body)
        monitor_weibo.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def get_monitor_wechat(request):
    obj = json.loads(request.body)
    plan_id = obj['planid']
    response = {}
    try:
        monitor_wechat = Monitor_wechat.objects.filter(plan_id=plan_id).order_by('id')
        response['list'] = json.loads(serializers.serialize("json", monitor_wechat))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def monitor_wechat_add(request):
    obj = json.loads(request.body)
    # print('obj', obj)
    name = obj['name']
    wxid = 'weixinid'
    status = 1
    plan_id = obj['planid']
    response = {}
    try:
        monitor_wechat = Monitor_wechat(name=name, wxid=wxid, status=status, plan_id=plan_id)
        monitor_wechat.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def monitor_wechat_delete(request):
    response = {}
    try:
        monitor_wechat = Monitor_wechat.objects.get(id=request.body)
        monitor_wechat.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")
