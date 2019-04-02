from django.db import models


# Create your models here.

# class Infolist(models.Model):
#     id = models.AutoField
#     author_name = models.CharField(max_length=50)
#     content = models.TextField()
#     time = models.CharField(max_length=30)
#     key_word = models.CharField(max_length=300)
#     url = models.CharField(max_length=300)
#     type = models.CharField(max_length=50)


class Allinfolist(models.Model):
    id = models.AutoField
    author_name = models.CharField(max_length=50)
    content = models.TextField()
    time = models.CharField(max_length=30)
    key_word = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    type = models.CharField(max_length=50)
    is_checked = models.BooleanField()
    sensitive_state = models.BooleanField()
    article_province = models.CharField(max_length=45)
    is_read = models.BooleanField()
    feelings = models.IntegerField()
    warning_level = models.IntegerField()
    source = models.CharField(max_length=45)
    similar_article = models.IntegerField(max_length=11)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    user_uuid = models.CharField(max_length=45)
    unique_together = ("name", "user_uuid")


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    area = models.CharField(max_length=54)
    character = models.CharField(max_length=54)
    event = models.CharField(max_length=54)
    exclude = models.CharField(max_length=54)
    group_id = models.IntegerField(max_length=54)
    ad_conf = models.CharField(max_length=54)
    user_uuid = models.CharField(max_length=45)


class WarningSetting(models.Model):
    id = models.AutoField
    warning_word = models.CharField(max_length=300)
    warning_content_type = models.CharField(max_length=10)
    warning_source_type = models.CharField(max_length=100)
    warning_similar_article = models.CharField(max_length=10)
    warning_region = models.CharField(max_length=100)
    warning_region_type = models.CharField(max_length=10)
    warning_source_website = models.CharField(max_length=10)
    warning_result_show = models.CharField(max_length=10)
    warning_forward_weibo = models.CharField(max_length=10)
    warning_relate_method = models.CharField(max_length=10)
    warning_match_method = models.CharField(max_length=10)
    warning_duplicate = models.CharField(max_length=10)
    warning_method_type = models.CharField(max_length=100)
    warning_start_time = models.CharField(max_length=45)
    warning_end_time = models.CharField(max_length=45)
    warning_interval = models.CharField(max_length=10)
    warning_weekend = models.CharField(max_length=10)
    plan_id = models.IntegerField(max_length=11)


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=None)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)


class Monitor_web(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=45)
    domain = models.CharField(max_length=255)
    status = models.BooleanField()
    plan_id = models.IntegerField(max_length=11)


class Monitor_weibo(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=45)
    uid = models.CharField(max_length=45)
    status = models.BooleanField()
    plan_id = models.IntegerField(max_length=11)


class Monitor_wechat(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=45)
    wxid = models.CharField(max_length=45)
    status = models.BooleanField()
    plan_id = models.IntegerField(max_length=11)
