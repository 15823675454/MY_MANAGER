from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(verbose_name='日志主题', max_length=50)
    teacher = models.CharField(verbose_name='教师编号', max_length=15)
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    isActive = models.BooleanField(verbose_name='状态', default=True)





