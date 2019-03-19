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


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    area = models.CharField(max_length=54)
    character = models.CharField(max_length=54)
    event = models.CharField(max_length=54)
    exclude = models.CharField(max_length=54)
    group_id = models.IntegerField(max_length=54)
    ad_conf = models.CharField(max_length=54)
