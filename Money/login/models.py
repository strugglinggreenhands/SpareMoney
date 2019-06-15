from django.db import models

# Create your models here.
# login/models.py

from django.db import models


class User(models.Model):
    """用户表"""

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    point = models.IntegerField(default='0')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Transaction(models.Model):
    """任务"""

    trans_type = (
        ('survey', '填写问卷'),
        ('morning', '叫早服务'),
        ('takeout', '带饭服务'),
        ('express', '代领快递'),
        ('drug', '代买药品'),
    )
    trans_num = models.AutoField(primary_key=True, unique=True)
    type = models.CharField(max_length=32, choices=trans_type)
    bonus = models.IntegerField(default='10')
    uploader = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    detail = models.CharField(max_length=512)
    c_time = models.DateTimeField(auto_now_add=True)
    d_time = models.DateTimeField(auto_now_add=True)
    is_accept = models.BooleanField(default='False')
    acceptor = models.CharField(max_length=256, default='None')
    is_finish = models.BooleanField(default='False')

    def __str__(self):
        return self.trans_num

    class Meta:
        ordering = ['trans_num']
        verbose_name = '任务'
        verbose_name_plural = '任务'