from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lano_end.models import WarningSetting

import json


@require_http_methods(['POST'])
@csrf_exempt
def add_warning(request):
    obj = json.loads(request.body)
    plan_id = obj['plan_id']
    warning_word = obj['warning_word']
    warning_content_type = obj['warning_content_type']
    warning_source_type = obj['warning_source_type']
    warning_similar_article = obj['warning_similar_article']
    warning_region = obj['warning_region']
    warning_region_type = obj['warning_region_type']
    warning_source_website = obj['warning_source_website']
    warning_result_show = obj['warning_result_show']
    warning_forward_weibo = obj['warning_forward_weibo']
    warning_relate_method = obj['warning_relate_method']
    warning_match_method = obj['warning_match_method']
    warning_duplicate = obj['warning_duplicate']
    warning_method_type = obj['warning_method_type']
    warning_start_time = obj['warning_start_time']
    warning_end_time = obj['warning_end_time']
    warning_interval = obj['warning_interval']
    warning_weekend = obj['warning_weekend']

    response = {}
    try:
        warning_exist = WarningSetting.objects.filter(plan_id=plan_id)
        print(warning_exist)
        if warning_exist:
            print("存在了")
            warning_exist = WarningSetting.objects.get(plan_id=plan_id)
            warning_exist.plan_id = plan_id
            warning_exist.warning_word = warning_word
            warning_exist.warning_content_type = warning_content_type
            warning_exist.warning_source_type = warning_source_type
            warning_exist.warning_similar_article = warning_similar_article
            warning_exist.warning_region = warning_region
            warning_exist.warning_region_type = warning_region_type
            warning_exist.warning_source_website = warning_source_website
            warning_exist.warning_result_show = warning_result_show
            warning_exist.warning_forward_weibo = warning_forward_weibo
            warning_exist.warning_relate_method = warning_relate_method
            warning_exist.warning_match_method = warning_match_method
            warning_exist.warning_duplicate = warning_duplicate
            warning_exist.warning_method_type = warning_method_type
            warning_exist.warning_start_time = warning_start_time
            warning_exist.warning_end_time = warning_end_time
            warning_exist.warning_interval = warning_interval
            warning_exist.warning_weekend = warning_weekend
            warning_exist.save()
        else:
            print("数据库没有")
            warning = WarningSetting(plan_id=plan_id,
                                     warning_word=warning_word,
                                     warning_content_type=warning_content_type,
                                     warning_source_type=warning_source_type,
                                     warning_similar_article=warning_similar_article,
                                     warning_region=warning_region,
                                     warning_region_type=warning_region_type,
                                     warning_source_website=warning_source_website,
                                     warning_result_show=warning_result_show,
                                     warning_forward_weibo=warning_forward_weibo,
                                     warning_relate_method=warning_relate_method,
                                     warning_match_method=warning_match_method,
                                     warning_duplicate=warning_duplicate,
                                     warning_method_type=warning_method_type,
                                     warning_start_time=warning_start_time,
                                     warning_end_time=warning_end_time,
                                     warning_interval=warning_interval,
                                     warning_weekend=warning_weekend, )
            warning.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return HttpResponse(json.dumps(response), content_type="application/json")
