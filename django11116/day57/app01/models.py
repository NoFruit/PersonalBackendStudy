from django.db import models

# Create your models here.

# class == 添加一个表
class UserInfo(models.Model):
    # var == 添加字段
    id = models.AutoField(primary_key=True) # 数据库中添加自增ID主键
    username = models.CharField(max_length=20) # == varchar(20)
    password = models.CharField(max_length=20)

# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)