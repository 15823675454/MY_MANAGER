from django.contrib import admin
from .models import *
# Register your models here.


# 学校
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_id', 'school_name']
    list_display_links = ['school_name']
    list_filter = ['school_name']
    list_editable = ['school_id']


# 教师
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacherid', 'teacher_name', 'gender', 'subject', 'phone', 'email', 'school']
    list_display_links = ['teacher_name']
    list_editable = ['subject']
    list_filter = ['gender', 'school_id', 'subject']
    search_fields = ['teacher_id', 'phone', 'subject', 'teacher_name']


# 学生
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'stu_id', 'stu_class', 'age', 'gender', 'teacher']
    list_display_links = ['name']
    list_editable = ['stu_id']
    list_filter = ['stu_class']
    search_fields = ['name', 'stu_id', 'stu_class', 'id']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)

