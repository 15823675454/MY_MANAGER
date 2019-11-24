from django.db import models

# Create your models here.


# 学校
class School(models.Model):
    school_name = models.CharField(verbose_name='校区', max_length=20, unique=True)
    school_id = models.CharField(verbose_name='校区编号', max_length=15, unique=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    isActive = models.BooleanField(verbose_name='状态', default=True)

    class Meta:
        db_table = 'school'
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school_name


# 教师注册列表
class Teacher(models.Model):

    # 姓名
    teacher_name = models.CharField(verbose_name='用户名', max_length=15, unique=True)
    # 科目
    subject = models.CharField(verbose_name='科目', max_length=10, default='')
    # 编号
    teacherid = models.CharField(verbose_name='员工编号', unique=True, max_length=20)
    # 密码
    password = models.CharField(verbose_name='密码', max_length=32)
    # 年龄
    age = models.CharField(verbose_name='年龄', max_length=5)
    # 邮箱
    email = models.EmailField(verbose_name='邮箱', max_length=60)
    # 性别
    gender = models.BooleanField(verbose_name='性别', default=True)
    # 电话
    phone = models.CharField(verbose_name='电话', max_length=20, unique=True)
    # 状态
    isActive = models.BooleanField(verbose_name='状态', default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 修改时间
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    # 登录时间
    login_time = models.DateTimeField(verbose_name='登录时间', null=True)
    # 外键
    school = models.ForeignKey(School)

    class Meta:
        # 当前model类对应的数据表表名
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name


# 学生
class Student(models.Model):
    stu_id = models.CharField(verbose_name='学号', max_length=15, unique=True)
    name = models.CharField(verbose_name='姓名', max_length=15)
    stu_class = models.CharField(verbose_name='班级', max_length=20, default='')
    age = models.CharField(verbose_name='年龄', max_length=5)
    gender = models.BooleanField(verbose_name='性别', default=True)
    teacher = models.ForeignKey(Teacher)
    phone = models.CharField(verbose_name='电话', max_length=20, default='')
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 修改时间
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    # 状态
    isActive = models.BooleanField(verbose_name='状态', default=True)

    class Meta:
        # 当前model类对应的数据表表名
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 家长
class Parent(models.Model):
    phone = models.CharField(verbose_name='电话', max_length=20, unique=True)
    username = models.CharField(verbose_name='姓名', max_length=15, default='')
    pwd = models.CharField(verbose_name='密码', max_length=32)
    gender = models.BooleanField(verbose_name='性别', default=True)
    email = models.EmailField(verbose_name='邮箱', null=True, default='')
    student = models.ForeignKey(Student)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 修改时间
    mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    # 登录时间
    login_time = models.DateTimeField(verbose_name='登录时间', null=True)
    # 状态
    isActive = models.BooleanField(verbose_name='状态', default=True)

    class Meta:
        # 当前model类对应的数据表表名
        db_table = 'parent'
        verbose_name = '家长'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



