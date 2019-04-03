from django.conf.urls import url
from lano_end.views import group_views
from lano_end.views import plan_views
from lano_end.views import switch_infolist_views
from lano_end.views import warning_views
from lano_end.views import user_views
from lano_end.views import direction_views
from lano_end.views import exclude_views

urlpatterns = [
    #url(r'get_infolist', infolist_views.get_infolist),
    url(r'create_group', group_views.create_group),
    url(r'get_groups', group_views.get_groups),

    url(r'create_ad_plan', plan_views.create_ad_plan),
    url(r'create_fast_plan', plan_views.create_fast_plan),
    url(r'get_plans', plan_views.get_plans),
    url(r'update_ad_plans', plan_views.update_plans),
    url(r'delete_group', group_views.delete_group),
    url(r'delete_plan', plan_views.delete_plan),

    url(r'switch_get_infolist', switch_infolist_views.get_infolist),

    url(r'add_warning', warning_views.add_warning),
    url(r'login', user_views.login),

    url(r'monitor_web_add', direction_views.monitor_web_add),
    url(r'get_monitor_web', direction_views.get_monitor_web),
    url(r'monitor_web_delete', direction_views.monitor_web_delete),
    url(r'get_monitor_weibo', direction_views.get_monitor_weibo),
    url(r'monitor_weibo_add', direction_views.monitor_weibo_add),
    url(r'monitor_weibo_delete', direction_views.monitor_weibo_delete),
    url(r'get_monitor_wechat', direction_views.get_monitor_wechat),
    url(r'monitor_wechat_add', direction_views.monitor_wechat_add),
    url(r'monitor_wechat_delete', direction_views.monitor_wechat_delete),
    url(r'get_exclude_web', exclude_views.get_exclude_web),
    url(r'exclude_web_add', exclude_views.exclude_web_add),
    url(r'exclude_web_delete', exclude_views.exclude_web_delete),
    url(r'get_exclude_weibo', exclude_views.get_exclude_weibo),
    url(r'exclude_weibo_add', exclude_views.exclude_weibo_add),
    url(r'exclude_weibo_delete', exclude_views.exclude_weibo_delete),
    url(r'get_exclude_wechat', exclude_views.get_exclude_wechat),
    url(r'exclude_wechat_add', exclude_views.exclude_wechat_add),
    url(r'exclude_wechat_delete', exclude_views.exclude_wechat_delete)
]
