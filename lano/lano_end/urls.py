from django.conf.urls import url
from lano_end.views import group_views
from lano_end.views import infolist_views
from lano_end.views import plan_views
from lano_end.views import switch_infolist_views
from lano_end.views import warning_views
from lano_end.views import user_views
from lano_end.views import direction_views

urlpatterns = [
    #url(r'get_infolist', infolist_views.get_infolist),
    url(r'create_group', group_views.create_group),
    url(r'get_groups', group_views.get_groups),
    url(r'create_plan', plan_views.create_plan),
    url(r'get_plans', plan_views.get_plans),
    url(r'update_plans', plan_views.update_plans),
    url(r'delete_group', group_views.delete_group),
    url(r'delete_plan', plan_views.delete_plan),
    url(r'switch_get_infolist', switch_infolist_views.get_infolist),
    url(r'add_warning', warning_views.add_warning),
    url(r'login', user_views.login),
    url(r'monitor_web_add',direction_views.monitor_web_add)
]
