from __future__ import unicode_literals
from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from lano_end.models import User
import json


def uuid_tostr(user):
    return user.uuid.__str__()


def user_format(user):
    return {
        'uuid': uuid_tostr(user),
        'username': user.username,
        'password': user.password,
        'name': user.name,
    }

# @require_http_methods(['POST'])
# @csrf_exempt
# def login(request):
#     obj = json.loads(request.body)
#     username = obj['username']
#     password = obj['password']
#     user = User.objects.get(username=username)
#     user = user_format(user)
#     response = {}
#     try:
#         if user:
#             if password == user['password']:
#                 user['token']='d787syv8dys8cas80d9s0a0d8f79ads56f7s4d56f879a8as89fd980s7dg'
#                 response['code'] = 0
#                 response['msg'] = '登录成功'
#                 response['data'] = {'user': user, 'token': user['token']}
#                 response['error_num'] = 0
#             else:
#                 response['code'] = '401'
#                 response['msg'] = '密码错误'
#                 response['data'] = {}
#                 response['error_num'] = 1
#         else:
#             response['code'] = 401
#             response['msg'] = '登录失败'
#             response['data'] = {}
#             response['error_num'] = 1
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['POST'])
@csrf_exempt
def login(request):
    obj = json.loads(request.body)
    username = obj['username']
    password = obj['password']
    response = {}
    try:
        user = User.objects.get(username=username)
        user = user_format(user)
        if password == user['password']:
            user['token'] = 'd787syv8dys8cas80d9s0a0d8f79ads56f7s4d56f879a8as89fd980s7dg'
            response['code'] = 0
            response['msg'] = '登录成功'
            response['data'] = {'user': user, 'token': user['token']}
            print('登录成功的user', user)
            response['error_num'] = 0
        else:
            response['code'] = '401'
            response['msg'] = '密码错误'
            response['data'] = {}
            response['error_num'] = 1
    except Exception:
        response['code'] = 401
        response['msg'] = '账号不存在'
        response['data'] = {}
        response['error_num'] = 1
    return HttpResponse(json.dumps(response), content_type="application/json")
