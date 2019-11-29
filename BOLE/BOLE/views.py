import json
from user.models import *
from django.http import *
from django.shortcuts import render
# project/views
from tools.logging_check import logging_check


def index(request):

    return render(request, 'login.html')


def index1(request):
    return render(request, 'index.html')


def head_1(request):
    return render(request, 'head.html')


def img_1(request, img):
    with open('../static/img/head/'+img, 'rb') as f:
        data = f.read()
    return render(request, 'static/img/head'+img)


def add_html(request):
    return render(request, 'add_student.html')


def student_art(request):
    return render(request, 'student_art.html')


def notfound(request):
    return HttpResponse('404 Not Found')


def calendar_index(request):
    return render(request, '日历.html')


# 删除学生
@logging_check('POST')
def delete_student(request, stu_id):
    stu_id = stu_id[4:]
    print('学号==========\n', stu_id)
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        if not data:
            res = {'code': 102, 'error': '请登录！'}
            return JsonResponse(res)
        username = data['teacher']
        try:
            teacher = Teacher.objects.get(teacher_name=username, isActive=True)
        except Exception as e:
            res = {'code': 803, 'error': '您没有权限!'}
            return JsonResponse(res)
        try:
            student = Student.objects.get(stu_id=stu_id, teacher=teacher, isActive=True)

        except Exception as e:
            res = {'code': 804, 'error': '您的该学生不存在!'}
            return JsonResponse(res)

        student.isActive = False
        student.save()
        res = {'code': 200, 'name': student.name}
        return JsonResponse(res)


# 修改学生
def update_student(request, stu_id):
    pass


# 修改教师基本信息界面
def teac_set_index(request):
    return render(request, 'teacher_setting.html')



