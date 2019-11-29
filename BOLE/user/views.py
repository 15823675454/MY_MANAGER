import datetime
import time
import jwt, json
from django.shortcuts import render
from hashlib import md5
from random import randint
from django.http import *
from .models import *
from django.db import transaction
# Create your views here.


# 检查登录
def check_login(request):
    print('==============检查登录函数被执行')
    if 'username' not in request.session or 'uid' not in request.session:
        # 有可能没登录
        print('session中无数据')
        # 检查cookies
        if 'username' not in request.COOKIES or 'uid' not in request.COOKIES:
            # 肯定没登录
            res = {'loginState': 0}
            print('没有cookie')
            return JsonResponse(res)
        else:
            # 回写session
            request.session['username'] = request.COOKIES['username']
            print('执行回写')
            request.session['uid'] = request.COOKIES['uid']
            print('--------', request.session['username'])
    res = {'loginState': 1, 'username': request.session['username']}
    return JsonResponse(res)


# 验证码更新
def send_code(request):
    code = verification()
    code = ''.join(code)
    return HttpResponse(code)


# 注册
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        student_id = request.POST.get('student_id')
        student = Student.objects.filter(stu_id=student_id)
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = encryption(password)
        # try:
        #     with transaction.atomic():
        user = Parent.objects.create(phone=phone, email=email, pwd=password, student=student[0])

        # except Exception as e:

            # print(e)
            # return HttpResponse('注册失败')
        return HttpResponse('注册成功')


# 登录入口
def door_view(request):
    return render(request, 'user/door.html')


# 用户校验
def check_name(request):
    user = request.GET.get('name')
    old_user = Parent.objects.filter(phone=user, isActive=True)
    if old_user:
        return HttpResponse('0')
    else:
        return HttpResponse('1')


# 学生校验
def check_student(request):
    student_id = request.GET.get('student_id')
    student = Student.objects.filter(stu_id=student_id, isActive=True)
    if student:
        return HttpResponse('1')
    else:
        return HttpResponse('0')


# 教师成功登录
def teacher_success(teacher):
    now_time = datetime.datetime.now()
    # 教师登录时间
    teacher.login_time = now_time
    teacher.save()

    item = {'identity': 'teacher', 'username': teacher.teacher_name, 'phone': teacher.phone, 'school': teacher.school.school_id}
    token = maketoken(item, 60 * 60 * 24, now_time).decode()
    res = {'code': 200, 'token': token, 'username': teacher.teacher_name}
    return res


# 家长成功登录
def parent_success(parent):
    now_time = datetime.datetime.now()
    # 教师登录时间
    parent[0].login_time = now_time
    parent[0].save()
    item = {'identity': 'parent', 'username': parent[0].username, 'phone': parent[0].phone, 'school': parent[
        0].student.teacher.school.school_id}
    token = maketoken(item, 60 * 60 * 24, now_time).decode()
    res = {'code': 200, 'token': token, 'username': parent[0].username}
    return res


# 登录
def log_view(request, school):
    if request.method == 'GET':
        if school == 'jbxq':
            return render(request, 'user/login.html')
        elif school == 'ybxq':
            return render(request, 'user/login1.html')
        elif school == 'jfb':
            return render(request, 'user/login2.html')
        else:
            raise Http404

    if request.method == 'POST':
        print('ssssssssss\n', school)
        data = request.body.decode('utf-8')
        data = json.loads(data)
        if not data:
            res = {'code': 400, 'error': 'no data'}
            return JsonResponse(res)
        # print('登录Post被调用')
        # 江北校区
        if school == 'jbxq':
            # print('6666666666666666666\n', data)
            school = School.objects.get(school_id=100001, isActive=True)
            identity = data['identity']
            phone = data['username']
            pwd = data['password']
            # print('====登录=========')
            # print(identity, phone, pwd)
            # 教师
            if identity == '1':
                try:
                    teacher = Teacher.objects.get(phone=phone, password=pwd, isActive=True, school=school)
                    # print('tttttttttt\n', teacher)
                except Exception as e:
                    return JsonResponse({'code':555, 'error': '该教师不存在!'})
                if teacher:
                    res = teacher_success(teacher)
                    # print('====教师登录成功')
                    # print(teacher[0].teacher_name)
                    return JsonResponse(res)
                else:
                    res = {'code': 405, 'error': '登录失败!'}
                    return JsonResponse(res)
            # 家长
            else:
                pwd = encryption(pwd)
                parent = Parent.objects.filter(phone=phone, isActive=True, pwd=pwd)
                if parent:
                    res = parent_success(parent)
                    return JsonResponse(res)
                else:
                    res = {'code': 405, 'error': '登录失败!'}
                    return JsonResponse(res)
        # 渝北校区
        elif school == 'ybxq':
            school = School.objects.get(school_id=100002, isActive=True)
            identity = data['identity']
            phone = data['username']
            pwd = data['password']
            # print('====登录=========')
            # print(identity, phone, pwd)
            # 教师
            if identity == '1':
                try:
                    teacher = Teacher.objects.get(phone=phone, password=pwd, isActive=True, school=school)
                    print('tttttttttt\n', teacher)
                except Exception as e:
                    return JsonResponse({'code': 555, 'error': '该教师不存在!'})
                if teacher:
                    res = teacher_success(teacher)
                    # print('====教师登录成功')
                    # print(teacher[0].teacher_name)
                    return JsonResponse(res)
                else:
                    res = {'code': 405, 'error': '登录失败!'}
                    return JsonResponse(res)
            # 家长
            else:
                pwd = encryption(pwd)
                parent = Parent.objects.filter(phone=phone, isActive=True, pwd=pwd)
                if parent:
                    res = parent_success(parent)
                    return JsonResponse(res)
                else:
                    res = {'code': 405, 'error': '登录失败!'}
                    return JsonResponse(res)
        # 解放碑校区
        elif school == 'jfb':
            school = School.objects.get(school_id=100003, isActive=True)
            identity = data['identity']
            phone = data['username']
            pwd = data['password']
            print('====登录=========')
            print(identity, phone, pwd)
            # 教师
            if identity == '1':
                try:
                    teacher = Teacher.objects.get(phone=phone, password=pwd, isActive=True, school=school)
                    print('tttttttttt\n', teacher)
                except Exception as e:
                    return JsonResponse({'code': 555, 'error': '该教师不存在!'})

                if teacher:
                    res = teacher_success(teacher)
                    # print('====教师登录成功')
                    # print(teacher[0].teacher_name)
                    return JsonResponse(res)
                else:
                    res = {'code': 405, 'error': '登录失败!'}
                    return JsonResponse(res)
            # 家长
            else:
                pwd = encryption(pwd)
                parent = Parent.objects.filter(phone=phone, isActive=True, pwd=pwd)
                if parent:
                    res = parent_success(parent)
                    return JsonResponse(res)
                else:
                    res = {'code': 405, 'error': '登录失败!'}
                    return JsonResponse(res)
        else:
            return HttpResponse('Not Found')


# 验证登录的用户名(教师或家长)
def login_check_name(requset):
    identity = requset.GET.get('identity')
    school = requset.GET.get('school')
    username = requset.GET.get('username')
    # print(identity, school, username)
    if school == 'jbxq':
        school = School.objects.get(school_id=100001, isActive=True)
    elif school == 'ybxq':
        school = School.objects.get(school_id=100002, isActive=True)
    elif school == 'jfb':
        school = School.objects.get(school_id=100003, isActive=True)
    # 教师
    if identity == '1':
        teacher = Teacher.objects.filter(phone=username, isActive=True, school=school)
        if teacher:
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    # 家长
    else:
        parent = Parent.objects.filter(phone=username, isActive=True)
        if parent:
            p_s_id = parent[0].student.teacher.school.school_id
        # print('-----家长--------')
        # print(p_s_id)
        else:
            return HttpResponse('0')
        if parent and p_s_id == school.school_id:
            return HttpResponse('1')
        else:
            return HttpResponse('0')


# 哈希加密
def encryption(password):
    sorlt = '*@mjcy&'
    hash = md5(sorlt.encode())
    hash.update(password.encode())
    passwd = hash.hexdigest()
    return passwd


# 验证码
def verification():
    str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    rand_verification = []
    for i in range(2):
        num1 = randint(0, 9)
        num2 = randint(0, len(str_list)-1)
        rand_verification.append(str(num1))
        rand_verification.append(str_list[num2])
    return rand_verification


# token
def maketoken(username, exp, now_datetime):
    key = '^&%*$#('
    now_t = time.time()
    payload = {'username': username, 'exp': int(now_t + exp), 'login_time': str(now_datetime)}
    return jwt.encode(payload, key, algorithm='HS256')









