from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from lano_end.models import Allinfolist
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import json


# this method get the sina_infolist
@require_http_methods(['GET'])
@csrf_exempt
def get_infolist(request):
    page_size = request.GET.get('page_size')
    page_num = request.GET.get('page_num')
    current_col = int(page_size) * (int(page_num) - 1)

    today = '2019-03-07'

    filter_params = json.loads(request.GET.get('filter_data'))
    print(filter_params['source_type_checkList'], type(filter_params['source_type_checkList']))
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
                elif(filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                            'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-time')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        print('www')
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
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

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('time')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('time')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
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

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('-similar_article')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-similar_article')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
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

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__contains=today).exclude(
                            content=None).order_by('-id')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):

                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-id')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='微信').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__contains=today,
                                                              ).exclude(
                            content=None).order_by('-id')

        # 24小时 time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'))
        elif (filter_params['time_range_radio'] == 2):
            # 文章排序：
            # 智能或降序
            if (filter_params['article_order_radio'] == 1 or filter_params['article_order_radio'] == 2):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-time')

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59')).exclude(
                            content=None).order_by('-time')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('-time')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('-time')

            # 时间升序
            if (filter_params['article_order_radio'] == 3):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('time')

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59')).exclude(
                            content=None).order_by('time')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('time')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('time')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('time')

            # 相似文章
            if (filter_params['article_order_radio'] == 4):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59')).exclude(
                            content=None).order_by('-similar_article')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('-similar_article')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-similar_article')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('-similar_article')

            # 采集顺序(降序)
            if (filter_params['article_order_radio'] == 5):
                # 敏感性
                # 非敏感
                if (filter_params['sensitive_attr_radio'] == 2):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-id')

                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=1, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59')).exclude(
                            content=None).order_by('-id')
                # 敏感
                elif (filter_params['sensitive_attr_radio'] == 3):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(sensitive_state=0, time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('-id')

                # 全部
                elif (filter_params['sensitive_attr_radio'] == 1):
                    # 媒体来源
                    if ('微信' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='微信').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              source='新浪新闻').exclude(
                            content=None).order_by('-id')
                    elif ('新闻' in filter_params['source_type_checkList'] and '微信' in filter_params[
                        'source_type_checkList']):
                        infolist = Allinfolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59'),
                                                              ).exclude(
                            content=None).order_by('-id')

        # 2天 time__range=('2018-12-28 00:00:00', '2018-12-29 23:59:59')
        elif (filter_params['time_range_radio'] == 3):
            # 智能或时间降序
            if (filter_params['article_order_radio'] == 0 | filter_params['article_order_radio'] == 1):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-28 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('-time')
            # 时间升序
            if (filter_params['article_order_radio'] == 2):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-28 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('time')

        # 3天
        elif (filter_params['time_range_radio'] == 4):
            # 智能或时间降序
            if (filter_params['article_order_radio'] == 0 | filter_params['article_order_radio'] == 1):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-27 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('-time')
            # 时间升序
            if (filter_params['article_order_radio'] == 2):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-27 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('time')

        # 7天
        elif (filter_params['time_range_radio'] == 5):
            # 智能或时间降序
            if (filter_params['article_order_radio'] == 0 | filter_params['article_order_radio'] == 1):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-22 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('-time')
            # 时间升序
            if (filter_params['article_order_radio'] == 2):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-22 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('time')
        # 10天
        elif (filter_params['time_range_radio'] == 6):
            # 智能或时间降序
            if (filter_params['article_order_radio'] == 0 | filter_params['article_order_radio'] == 1):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-19 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('-time')
            # 时间升序
            if (filter_params['article_order_radio'] == 2):
                infolist = Allinfolist.objects.filter(
                    time__range=('2018-12-19 00:00:00', '2018-12-29 23:59:59')).exclude(
                    content=None).order_by('time')

        else:
            infolist = Allinfolist.objects.order_by('id').exclude(content=None)

        list = infolist[current_col:current_col + int(page_size)]
        response['list_count'] = infolist.count()
        response['list'] = json.loads(serializers.serialize("json", list))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# this method get the sina_infolist
# @require_http_methods(['GET'])
# @csrf_exempt
# def get_infolist(request):
#     page_size = request.GET.get('page_size')
#     page_num = request.GET.get('page_num')
#     current_col = int(page_size) * (int(page_num) - 1)
#
#     today = '2018-12-29'
#
#     filter_params = json.loads(request.GET.get('filter_data'))
#     print(filter_params)
#     response = {}
#     infolist = {}
#     list = {}
#     try:
#         # 今日
#         if (filter_params['time_range_radio'] == 1):
#             # 智能或时间降序
#             if (filter_params['result_show_radio'] == 0 | filter_params['result_show_radio'] == 1):
#                 infolist = Infolist.objects.filter(time__contains=today).exclude(content=None).order_by('-time')
#                 list = infolist[current_col:current_col + int(page_size)]
#             # 时间升序
#             if (filter_params['result_show_radio'] == 2):
#                 infolist = Infolist.objects.filter(time__contains=today).exclude(content=None).order_by('time')
#                 list = infolist[current_col:current_col + int(page_size)]
#
#         # 24小时
#         elif (filter_params['time_range_radio'] == 2):
#             # 智能或时间降序
#             if (filter_params['result_show_radio'] == 0 | filter_params['result_show_radio'] == 1):
#                 infolist = Infolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('-time')
#                 list = infolist[current_col:current_col + int(page_size)]
#             # 时间升序
#             if (filter_params['result_show_radio'] == 2):
#                 infolist = Infolist.objects.filter(time__range=('2018-12-29 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('time')
#                 list = infolist[current_col:current_col + int(page_size)]
#
#         # 2天
#         elif (filter_params['time_range_radio'] == 3):
#             # 智能或时间降序
#             if (filter_params['result_show_radio'] == 0 | filter_params['result_show_radio'] == 1):
#                 infolist = Infolist.objects.filter(time__range=('2018-12-28 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('-time')
#                 list = infolist[current_col:current_col + int(page_size)]
#             # 时间升序
#             if (filter_params['result_show_radio'] == 2):
#                 infolist = Infolist.objects.filter(time__range=('2018-12-28 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('time')
#                 list = infolist[current_col:current_col + int(page_size)]
#
#         # 3天
#         elif (filter_params['time_range_radio'] == 4):
#             # 智能或时间降序
#             if (filter_params['result_show_radio'] == 0 | filter_params['result_show_radio'] == 1):
#                 infolist = Infolist.objects.filter(time__range=('2018-12-27 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('-time')
#                 list = infolist[current_col:current_col + int(page_size)]
#             # 时间升序
#             if (filter_params['result_show_radio'] == 2):
#                 infolist = Infolist.objects.filter(time__range=('2018-12-27 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('time')
#                 list = infolist[current_col:current_col + int(page_size)]
#
#         # 7天
#         elif (filter_params['time_range_radio'] == 5):
#             # 智能或时间降序
#             if (filter_params['result_show_radio'] == 0 | filter_params['result_show_radio'] == 1):
#                 infolist = Infolist.objects.filter(
#                     time__range=('2018-12-22 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('-time')
#                 list = infolist[current_col:current_col + int(page_size)]
#             # 时间升序
#             if (filter_params['result_show_radio'] == 2):
#                 infolist = Infolist.objects.filter(
#                     time__range=('2018-12-22 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('time')
#                 list = infolist[current_col:current_col + int(page_size)]
#         # 10天
#         elif (filter_params['time_range_radio'] == 6):
#             # 智能或时间降序
#             if (filter_params['result_show_radio'] == 0 | filter_params['result_show_radio'] == 1):
#                 infolist = Infolist.objects.filter(
#                     time__range=('2018-12-19 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('-time')
#                 list = infolist[current_col:current_col + int(page_size)]
#             # 时间升序
#             if (filter_params['result_show_radio'] == 2):
#                 infolist = Infolist.objects.filter(
#                     time__range=('2018-12-19 00:00:00', '2018-12-29 23:59:59')).exclude(
#                     content=None).order_by('time')
#                 list = infolist[current_col:current_col + int(page_size)]
#
#         else:
#             infolist = Infolist.objects.order_by('id').exclude(content=None)[current_col:current_col + int(page_size)]
#
#         response['list_count'] = infolist.count()
#         response['list'] = json.loads(serializers.serialize("json", list))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#
#     return JsonResponse(response)
