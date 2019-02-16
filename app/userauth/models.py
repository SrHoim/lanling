from django.db import models

# Create your models here.

class User(models.Model):
    phone = models.CharField(max_length=11)  # 必填 max_length
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=10,default='null',)
    img = models.ImageField(upload_to='userimg',default='null')

class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    con = models.CharField(verbose_name='内容', max_length=20000)
    aname = models.CharField(verbose_name='作者', max_length=20)