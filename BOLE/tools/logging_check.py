import jwt
from django.http import JsonResponse

from user.models import Teacher,Parent
TOKEN_KEY = '^&%*$#('


def logging_check(*methods):
    def _logging_check(func):
        def wrapper(request, *args, **kwargs):
            # 逻辑判断
            # 判断当前请求是否需要较验
            # 取出token
            # 需要交验，如何校验
            # 1.请求方法没传
            if not methods:
                return func(request, *args, **kwargs)

            else:
                # 2.当前请求方法不在参数中
                if request.method not in methods:
                    return func(request, *args, **kwargs)
            # 取出token
            token = request.META.get('HTTP_AUTHORIZATION')
            # 如果没有token
            if not token:
                result = {'code': 206, 'error': 'Please login'}
                return JsonResponse(result)
            try:
                # 因为token值可能被更改
                res = jwt.decode(token, TOKEN_KEY, algorithms='HS256')
            except Exception as e:
                print(e)
                result = {'code': 207, 'error': 'Please login'}
                return JsonResponse(result)
            username = res['username']
            # 教师令牌
            if username['identity'] == 'teacher':
                # 取出token里的login_time
                login_time = res.get('login_time')
                try:
                    teacher = Teacher.objects.filter(phone=username['phone'], teacher_name=username['username'])[0]
                except Exception as e:
                    result = {'code': 209, 'error': '身份验证不通过'}
                    return JsonResponse(result)
                if login_time:
                    if login_time != str(teacher.login_time):
                        print('++++++++logintime+++++++\n', login_time, teacher.login_time)
                        result = {'code': 20106, 'error': 'Other people login !!! Please login again!'}
                        return JsonResponse(result)

                request.user = teacher
                return func(request, *args, **kwargs)
            # 家长令牌
            elif username['identity'] == 'parent':
                # 取出token里的login_time
                login_time = res.get('login_time')
                try:
                    parent = Parent.objects.filter(phone=username['phone'], username=username['username'])[0]
                except Exception as e:
                    result = {'code': 209, 'error': '身份验证不通过'}
                    return JsonResponse(result)
                if login_time:
                    if login_time != str(parent.login_time):
                        result = {'code': 20106, 'error': 'Other people login !!! Please login again!'}
                        return JsonResponse(result)
                request.user = parent
                return func(request, *args, **kwargs)
            # 身份不存在
            else:
                result = {'code': 208, 'error': 'identity not cross'}
                return JsonResponse(result)

        return wrapper
    return _logging_check


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

