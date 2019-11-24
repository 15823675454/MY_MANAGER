import json

import jwt
from django.shortcuts import render
from django.http import *
from tools.logging_check import get_user_by_request, logging_check
from user.models import *
from score.models import *
# Create your views here.
TOKEN_KEY = '^&%*$#('


# 检查token
def get_user_by_request(request):
    # 尝试获取用户身份
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        # 用户未登录
        return None
    try:
        res = jwt.decode(token, TOKEN_KEY, algorithms='HS256')
    except Exception as e:
        print(e)
        return None
    data = res['username']
    identity = data['identity']
    if identity == 'teacher':
        teacher = Teacher.objects.filter(teacher_name=data['username'], phone=data['phone'])[0]
        if teacher and teacher.school.school_id == data['school']:
            # 通过
            return [teacher, '1']
        else:
            return None
    elif identity == 'parent':
        parent = Parent.objects.filter(username=data['username'], phone=data['phone'])[0]
        if parent:
            # 通过
            return [parent, '0']
        else:
            return None


def teacher_info(request):
    # res = request.res
    return render(request, 'interior/index.html')


# 返回该教师的所有学生
@logging_check('POST')
def return_all_stu_info(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        # print('学生---', data)
        if not data:
            res = {'code': 2010, 'error': 'not data'}
            return JsonResponse(res)
        user = get_user_by_request(request)
        if user:
            # 教师
            if user[1] == '1':
                all_stu = Student.objects.filter(teacher=user[0])
                # print(all_stu)
                res = {'code': 200, 'data': [], 'class_list': []}

                for i in all_stu:
                    try:
                        stu_score = ArtWork.objects.filter(student=i.stu_id)[0]
                        score = stu_score.score
                    except Exception as e:
                        score = 0
                    if i.stu_class not in res['class_list']:
                        res['class_list'].append(i.stu_class)
                    item={}
                    # print(i)
                    item['stu_id'] = i.stu_id
                    item['name'] = i.name
                    item['stu_class'] = i.stu_class
                    item['score'] = score
                    # item['score'] = {'语文': stu_score.chinese, '数学': stu_score.math, '英语': stu_score.english,
                    #                  '物理': stu_score.physical, '化学': stu_score.chemistry, '生物': stu_score.biological,
                    #                  '政治': stu_score.political, '历史': stu_score.history, '地理': stu_score.geography,
                    #                  '体育': stu_score.sports, '美术': stu_score.art}
                    res['data'].append(item)
                # 待写--排序res['data']根据成绩排序
                selectionSort(res['data'])

                return JsonResponse(res)
            # 家长
            else:
                pass
        else:
            res = {'code': 2011, 'error': 'the user not exists'}
            return JsonResponse(res)


# 单独一个班级的所有学生 w_class-->班级
@logging_check('POST')
def one_class(request, w_class):
    if request.method == 'POST':
        print('单个班级函数被调用', w_class)
        all_stu = Student.objects.filter(stu_class=w_class)
        res = {'code': 200, 'data': []}
        for i in all_stu:
            item = {}
            try:
                stu_score = ArtWork.objects.filter(student=i.stu_id)[0]
                score = stu_score.score
            except Exception as e:
                score = 0
            item = {}
            # print(i)
            item['stu_id'] = i.stu_id
            item['name'] = i.name
            item['stu_class'] = i.stu_class
            item['score'] = score
            res['data'].append(item)
        # 排序res['data']根据成绩排序
        selectionSort(res['data'])

    return JsonResponse(res)


# 选择排序
def selectionSort(nums):
    for i in range(0, len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j]['score'] > nums[min]['score']:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


# 单个学生信息
@logging_check('POST')
def student_info(request, stu_id):
    if request.method == 'POST':
        print('学生个人信息')
        try:
            student = Student.objects.get(stu_id=stu_id)
        except Exception as e:
            res = {'code': 404, 'error': 'not found student'}
            return JsonResponse(res)
        res = {'code': 200, 'data': {'name': student.name, 'stu_id': student.stu_id, 'stu_class': student.stu_class,
                                     'age': student.age, 'gender': student.gender, 'teacher':
                                         student.teacher.teacher_name, 'phone': student.phone}}
        return JsonResponse(res)


# 所有学生作品
@logging_check('POST')
def student_art(request):
    if request.method == 'POST':
        teacher = request.user
        all_student = Student.objects.filter(teacher=teacher)
        res = {'code': 200, 'data': []}
        for stu in all_student:
            item = {}
            item['name'] = stu.stu_id
            item['art'] = []
            art = ArtWork.objects.filter(student=stu.stu_id)
            for i in art:
                img_item = {}
                img_item['score'] = i.score
                img_item['img'] = str(i.img)
                item['art'].append(img_item)
            # 先对每个学生作品成绩排序 高--低
            selectionSort(item['art'])
            res['data'].append(item)
        # 成绩排序
        """{'data':
                    [
                        {'name':'xxx',
                         'art':[{'score': 88, 'img': 'kldf.jpg'},{'score':77, 'img': 'xxx.jpg'}]
                        }
                    ]
           }
                    """
        # 排序
        # for i in range(len(res['data'])):
        #     min = res['data'][i]['art'][0]['score']
        #     for j in range(1, len(res['data'])):
        #         if res['data'][j]['art'][0]['score'] > min:
        #             res['data'][i],res['data'][j] = res['data'][j],res['data'][i]
        art_sort(res)
        return JsonResponse(res)


# 学生作品排序
def art_sort(res):
    for i in range(len(res['data'])):
        if len(res['data'][i]['art']) > 0:
            min = res['data'][i]['art'][0]['score']
        for j in range(i + 1, len(res['data'])):
            if len(res['data'][j]['art']) > 0:
                if res['data'][j]['art'][0]['score'] > min:
                    res['data'][i], res['data'][j] = res['data'][j], res['data'][i]


def add_student(request):
    return None











