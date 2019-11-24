from django.db import models

# Create your models here.


# 学生成绩
class StudentScore(models.Model):
    student = models.CharField(verbose_name='学号', max_length=15)
    chinese = models.DecimalField(verbose_name='语文', max_digits=5, decimal_places=2, default=0)
    math = models.DecimalField(verbose_name='数学', max_digits=5, decimal_places=2, default=0)
    english = models.DecimalField(verbose_name='英语', max_digits=5, decimal_places=2, default=0)
    physical = models.DecimalField(verbose_name='物理', max_digits=5, decimal_places=2, default=0)
    chemistry = models.DecimalField(verbose_name='化学', max_digits=5, decimal_places=2, default=0)
    biological = models.DecimalField(verbose_name='生物', max_digits=5, decimal_places=2, default=0)
    political = models.DecimalField(verbose_name='政治', max_digits=5, decimal_places=2, default=0)
    history = models.DecimalField(verbose_name='历史', max_digits=5, decimal_places=2, default=0)
    geography = models.DecimalField(verbose_name='地理', max_digits=5, decimal_places=2, default=0)
    sports = models.DecimalField(verbose_name='体育', max_digits=5, decimal_places=2, default=0)
    art = models.DecimalField(verbose_name='美术', max_digits=5, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    isActive = models.BooleanField(verbose_name='状态', default=True)

    class Meta:
        # 当前model类对应的数据表表名
        db_table = 'score'
        verbose_name = '学生成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student


# 美术作品
class ArtWork(models.Model):
    student = models.CharField(verbose_name='学号', max_length=15)
    img = models.ImageField(verbose_name='学生作品', upload_to='picture')
    score = models.DecimalField(verbose_name='评分', max_digits=5, decimal_places=2)
    create_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    isActive = models.BooleanField(verbose_name='状态', default=True)

    class Meta:
        # 当前model类对应的数据表表名
        db_table = 'art'
        verbose_name = '学生作品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student



