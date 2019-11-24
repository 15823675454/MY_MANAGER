from django.conf.urls import url
from . import views
# 路径：interior/urls
urlpatterns = [
    # 老师登录成功后的显示界面
    url(r'^teacher/\w{2,40}', views.teacher_info),
    # ajax请求所有该老师的学生信息
    url(r'^all_student', views.return_all_stu_info),
    url(r'^one_class/(?P<w_class>.+)', views.one_class),
    url(r'^student/(?P<stu_id>\d+)', views.student_info),
    url(r'^student$', views.student_art),
    url(r'^student/add$', views.add_student)

]




