from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from lano_end.models import Allinfolist
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import json
import datetime
import re


def chooseTimeRange(infolist, filter_params):
    now = datetime.datetime.strptime("2019-03-07 00:00:00", "%Y-%m-%d %H:%M:%S")
    today = now.strftime('%Y-%m-%d')
    # 1.今日  2.24小时  3.2天  4.3天  5.7天  6.10天  7.自定义
    if (any(filter_params['time_value'])):

        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        user_defined_time_start = datetime.datetime.strptime(filter_params['time_value'][0], UTC_FORMAT)
        user_defined_time_end = datetime.datetime.strptime(filter_params['time_value'][1], UTC_FORMAT)
        print("自定义时间", user_defined_time_start, user_defined_time_end)
        user_defined_time_start = user_defined_time_start + datetime.timedelta(hours=8)
        user_defined_time_end = user_defined_time_end + datetime.timedelta(hours=8)
        return infolist.filter(time__range=(user_defined_time_start, user_defined_time_end))
    return{
        1: infolist.filter(time__contains=today),
        2: infolist.filter(time__range=(now, now+datetime.timedelta(hours=24))),
        3: infolist.filter(time__range=(now, now+datetime.timedelta(days=2))),
        4: infolist.filter(time__range=(now, now+datetime.timedelta(days=3))),
        5: infolist.filter(time__range=(now, now+datetime.timedelta(days=7))),
        6: infolist.filter(time__range=(now, now+datetime.timedelta(days=10))),
    }.get(filter_params['time_range_radio'], 'error')


def chooseArticleOrder(infolist, filter_params):
    # 1.智能排序  2.时间降序  3时间升序  4.相似文章  5.采集顺序
    return{
        1: infolist,
        2: infolist.order_by('-time'),
        3: infolist.order_by('time'),
        4: infolist.order_by('-similar_article'),
        5: infolist,
    }.get(filter_params['article_order_radio'], 'error')


def chooseSensitiveState(infolist, filter_params):
    print("filter_params['sensitive_attr_radio']", filter_params['sensitive_attr_radio'])
    if filter_params['sensitive_attr_radio'] == 1:
        return infolist
    elif filter_params['sensitive_attr_radio'] == 2:
        filter_params['sensitive_attr_radio']=filter_params['sensitive_attr_radio']-2
        return infolist.exclude(sensitive_state=filter_params['sensitive_attr_radio'])
    elif filter_params['sensitive_attr_radio'] == 3:
        filter_params['sensitive_attr_radio'] = filter_params['sensitive_attr_radio'] - 2
        return infolist.exclude(sensitive_state=filter_params['sensitive_attr_radio'])


def filtkeywords(infolist, current_plan):
    # infolist=infolist.filter(key_word__reg=current_plan['fields']['ad_match'])  # 关键字筛选
    print('current_plan',current_plan)
    print('infolist', infolist)

    ad_name = current_plan['fields']['ad_match']
    ad_match = current_plan['fields']['ad_match']
    ad_exclude = current_plan['fields']['ad_exclude']
    fast_area = current_plan['fields']['fast_area']
    fast_character = current_plan['fields']['fast_character']
    fast_event = current_plan['fields']['fast_event']
    fast_exclude = current_plan['fields']['fast_exclude']
    # 是否是高级配置
    if ad_name is not None:
        this_is_advance_plan = True
    else:
        this_is_advance_plan = False
    #高级配置
    if this_is_advance_plan is True:
        print('ad_match', ad_match)
        keywords_regex = r"[\u4e00-\u9fa5]+"
        keywords_pattern = re.compile(keywords_regex)
        keywords_in_ad_match=keywords_pattern.findall(ad_match)
        print('keywords_in_ad_match', keywords_in_ad_match)
        signs_regex = r"[+|]+"
        signs_pattern = re.compile(signs_regex)
        signs_in_ad_match =signs_pattern.findall(ad_match)
        print('signs_in_ad_match', signs_in_ad_match)


    #快速配置
    else:
        print('快速', current_plan)
        keywords_regex = r"[\u4e00-\u9fa5]+"
        keywords_pattern = re.compile(keywords_regex)
        keywords_fast_area = keywords_pattern.findall(fast_area)
        keywords_fast_character = keywords_pattern.findall(fast_character)
        keywords_fast_event = keywords_pattern.findall(fast_event)
        keywords_fast_exclude = keywords_pattern.findall(fast_exclude)
        print('keywords_fast_area', keywords_fast_area)
        signs_regex = r"[+|]"
        signs_pattern = re.compile(signs_regex)
        signs_in_fast_area = signs_pattern.findall(fast_area)
        signs_in_fast_character = signs_pattern.findall(fast_character)
        signs_in_fast_event = signs_pattern.findall(fast_event)
        # signs_in_fast_exclude = signs_pattern.findall(fast_exclude)
        print('signs_in_fast_area', signs_in_fast_area)
        if signs_in_fast_area[0] == '+':
            for i in keywords_fast_area:
                infolist = infolist.filter(content__contains=i)
        elif signs_in_fast_area[0] == '|':
            str = 'infolist = infolist.filter(content__contains=\'{}\')'.format(keywords_fast_area[0])
            for i in keywords_fast_area:
                str = str + '|infolist.filter(content__contains=\'{}\')'.format(i)
            print('str',str)
            eval("str")
            print('infolist',infolist)
            # infolist = infolist.filter(content__contains='妈妈') | infolist.filter(
            #     content__contains='妈妈') | infolist.filter(content__contains='学校')

        if signs_in_fast_character[0] == '+':
            for i in keywords_fast_character:
                infolist = infolist.filter(content__contains=i)
        else:
            infolist = infolist.filter(content__contains=signs_in_fast_area)
        if signs_in_fast_event[0] == '+':
            for i in keywords_fast_event:
                infolist = infolist.filter(content__contains=i)
        else:
            infolist = infolist.filter(content__contains=signs_in_fast_area)
        for i in keywords_fast_exclude:
            infolist = infolist.exclude(content__contains=i)

    print('filtkeywords ad_match, ad_exclude, fast_area, fast_character, fast_event, fast_exclude'
          , ad_match, ad_exclude, fast_area, fast_character, fast_event, fast_exclude)

    return infolist


# this method get the sina_infolist
@require_http_methods(['GET'])
@csrf_exempt
def get_infolist(request):
    page_size = request.GET.get('page_size')  # 一页有多少信息
    page_num = request.GET.get('page_num')  # 页数
    current_col = int(page_size) * (int(page_num) - 1)  #当前这一页的30条数据
    filter_params = json.loads(request.GET.get('filter_data'))  # 筛选参数
    current_plan = json.loads(request.GET.get('current_plan'))
    print('current_plan.fields', current_plan['fields'])
    print('filter_params', filter_params)
    response = {}
    try:
        # if current_plan['fields']['name'] == 'initialplan':
        #     # infolist = chooseTimeRange(filter_params['time_range_radio'], user_defined_time_start, user_defined_time_end)
        #     # 初始化infolist，微信 新闻源，时间降序，排除空内容
        #     infolist = Allinfolist.objects.exclude(content=None)
        #     infolist = chooseTimeRange(infolist, filter_params)  # 经过 时间 筛选后的infolist
        #     infolist = chooseArticleOrder(infolist, filter_params)  # 经过 排序 筛选后的infolist
        #     infolist = infolist.filter(source__in=filter_params['source_type_checkList'])  # 经过 来源类型 筛选后的infolist
        #     infolist = chooseSensitiveState(infolist, filter_params)  # 经过 敏感 筛选后的infolist
        # else:
        infolist = Allinfolist.objects.exclude(content=None)
        infolist = chooseTimeRange(infolist, filter_params)  # 经过 时间 筛选后的infolist
        infolist = chooseArticleOrder(infolist, filter_params)  # 经过 排序 筛选后的infolist
        infolist = infolist.filter(source__in=filter_params['source_type_checkList'])  # 经过 来源类型 筛选后的infolist
        infolist = chooseSensitiveState(infolist, filter_params)  # 经过 敏感 筛选后的infolist
        infolist = filtkeywords(infolist,current_plan)


        list = infolist[current_col:current_col + int(page_size)]
        response['list_count'] = infolist.count()
        response['list'] = json.loads(serializers.serialize("json", list))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
