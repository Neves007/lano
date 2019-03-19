from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from lano_end.models import Allinfolist
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import json
import datetime


def filter_conditions(filter_params, time_start, time_end):
    infolist = {}
    print(filter_params)
    # 文章排序：
    # 智能或降序
    if (filter_params['article_order_radio'] == 1 or filter_params['article_order_radio'] == 2):
        # 敏感性
        # 非敏感
        print('qqqq')
        if (filter_params['sensitive_attr_radio'] == 2):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end), source='微信').exclude(
                    content=None).order_by('-time')

            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end), source='新浪新闻').exclude(
                    content=None).order_by('-time')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end)).exclude(content=None).order_by('-time')
        # 敏感
        if (filter_params['sensitive_attr_radio'] == 3):

            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end), source='微信').exclude(content=None).order_by('-time')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end), source='新浪新闻').exclude(content=None).order_by('-time')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end)).exclude(content=None).order_by('-time')

        # 全部
        if (filter_params['sensitive_attr_radio'] == 1):
            print('eeeee')
            print(len(filter_params['source_type_checkList']) >= 2)

            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='微信').exclude(
                    content=None).order_by('-time')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='新浪新闻').exclude(
                    content=None).order_by('-time')
            if (len(filter_params['source_type_checkList']) >= 2):
                print('wwww')
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                ).exclude(
                    content=None).order_by('-time')
                print(infolist)

    # 时间升序
    elif (filter_params['article_order_radio'] == 3):
        # 敏感性
        # 非敏感
        if (filter_params['sensitive_attr_radio'] == 2):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end),
                                                      source='微信').exclude(
                    content=None).order_by('time')

            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end),
                                                      source='新浪新闻').exclude(
                    content=None).order_by('time')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end)).exclude(
                    content=None).order_by('time')
        # 敏感
        if (filter_params['sensitive_attr_radio'] == 3):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      source='微信').exclude(
                    content=None).order_by('time')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      source='新浪新闻').exclude(
                    content=None).order_by('time')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      ).exclude(
                    content=None).order_by('time')

        # 全部
        if (filter_params['sensitive_attr_radio'] == 1):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='微信').exclude(
                    content=None).order_by('time')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='新浪新闻').exclude(
                    content=None).order_by('time')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                ).exclude(
                    content=None).order_by('time')

    # 相似文章
    elif (filter_params['article_order_radio'] == 4):
        # 敏感性
        # 非敏感
        if (filter_params['sensitive_attr_radio'] == 2):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end),
                                                      source='微信').exclude(
                    content=None).order_by('-similar_article')

            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end),
                                                      source='新浪新闻').exclude(
                    content=None).order_by('-similar_article')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end)).exclude(
                    content=None).order_by('-similar_article')
        # 敏感
        if (filter_params['sensitive_attr_radio'] == 3):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      source='微信').exclude(
                    content=None).order_by('-similar_article')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      source='新浪新闻').exclude(
                    content=None).order_by('-similar_article')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      ).exclude(
                    content=None).order_by('-similar_article')

        # 全部
        if (filter_params['sensitive_attr_radio'] == 1):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='微信').exclude(
                    content=None).order_by('-similar_article')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='新浪新闻').exclude(
                    content=None).order_by('-similar_article')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                ).exclude(
                    content=None).order_by('-similar_article')

    # 采集顺序(降序)
    elif (filter_params['article_order_radio'] == 5):
        # 敏感性
        # 非敏感
        if (filter_params['sensitive_attr_radio'] == 2):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end),
                                                      source='微信').exclude(
                    content=None).order_by('-id')

            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end),
                                                      source='新浪新闻').exclude(
                    content=None).order_by('-id')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=(
                    time_start, time_end)).exclude(
                    content=None).order_by('-id')
        # 敏感
        if (filter_params['sensitive_attr_radio'] == 3):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      source='微信').exclude(
                    content=None).order_by('-id')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      source='新浪新闻').exclude(
                    content=None).order_by('-id')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=(
                    time_start, time_end),
                                                      ).exclude(
                    content=None).order_by('-id')

        # 全部
        if (filter_params['sensitive_attr_radio'] == 1):
            # 媒体来源
            if ('微信' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='微信').exclude(
                    content=None).order_by('-id')
            if ('新闻' in filter_params['source_type_checkList']):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                    source='新浪新闻').exclude(
                    content=None).order_by('-id')
            if (len(filter_params['source_type_checkList']) > 1):
                infolist = Allinfolist.objects.filter(
                    time__range=(time_start, time_end),
                ).exclude(
                    content=None).order_by('-id')

    return infolist

# this method get the sina_infolist
@require_http_methods(['GET'])
@csrf_exempt
def get_infolist(request):
    page_size = request.GET.get('page_size')
    page_num = request.GET.get('page_num')
    current_col = int(page_size) * (int(page_num) - 1)
    today = '2019-03-07'
    filter_params = json.loads(request.GET.get('filter_data'))
    time_start = ''
    time_end = ''
    if(any(filter_params['time_value'])):
        print(filter_params['source_type_checkList'], filter_params['time_value'])

        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        time_start = datetime.datetime.strptime(filter_params['time_value'][0], UTC_FORMAT)
        time_end = datetime.datetime.strptime(filter_params['time_value'][1], UTC_FORMAT)

        time_start = time_start + datetime.timedelta(hours=8)
        time_end = time_end + datetime.timedelta(hours=8)

        print(time_start, time_end)
    response = {}
    infolist = {}
    try:
        # 今日
        if (filter_params['time_range_radio'] == 1):
            # 文章排序：
            # 智能或降序
            if (filter_params['article_order_radio'] == 1 or filter_params['article_order_radio'] == 2):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-time')

                    elif ('新闻' in filter_params['source_type_checkList'] ):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-time')

                    elif('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('-time')
                # 敏感
                if(filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-time')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-time')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                            'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-time')

                # 全部
                if (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(content=None).order_by('-time')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(content=None).order_by('-time')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today).exclude(content=None).order_by('-time')

            # 时间升序
            if (filter_params['article_order_radio'] == 3):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('time')

                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('time')
                # 敏感
                if (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('time')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('time')

                # 全部
                if (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('time')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              ).exclude(
                            content=None).order_by('time')

            #相似文章
            if (filter_params['article_order_radio'] == 4):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')

                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('-similar_article')
                # 敏感
                if (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-similar_article')

                # 全部
                if (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-similar_article')

            #采集顺序(降序)
            if (filter_params['article_order_radio'] == 5):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-id')

                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('-id')
                # 敏感
                if (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-id')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):

                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-id')

                # 全部
                if (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-id')
                    if ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    if ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-id')
        # 24小时 time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'))
        elif (filter_params['time_range_radio'] == 2):
            infolist = filter_conditions(filter_params, '2018-12-29 00:00:00', '2018-12-29 23:59:59')
        # 2天 time__range=('2018-12-28 00:00:00', '2018-12-29 23:59:59')
        elif (filter_params['time_range_radio'] == 3):
            infolist = filter_conditions(filter_params, '2018-12-28 00:00:00', '2018-12-29 23:59:59')
        # 3天 '2018-12-27 00:00:00', '2018-12-29 23:59:59'
        elif (filter_params['time_range_radio'] == 4):
            infolist = filter_conditions(filter_params, '2018-12-27 00:00:00', '2018-12-29 23:59:59')
        # 7天 '2018-12-22 00:00:00', '2018-12-29 23:59:59'
        elif (filter_params['time_range_radio'] == 5):
            infolist = filter_conditions(filter_params, '2018-12-22 00:00:00', '2018-12-29 23:59:59')
        # 10天 2018-12-19 00:00:00', '2018-12-29 23:59:59
        elif (filter_params['time_range_radio'] == 6):
            infolist = filter_conditions(filter_params, '2018-12-19 00:00:00', '2018-12-29 23:59:59')
        else:
            infolist = filter_conditions(filter_params, time_start, time_end)

        list = infolist[current_col:current_col + int(page_size)]
        response['list_count'] = infolist.count()
        response['list'] = json.loads(serializers.serialize("json", list))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

