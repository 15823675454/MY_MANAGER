from django.conf.urls import url
from . import views
# 路径：user/urls
urlpatterns = [
    url(r'^reg', views.reg_view),
    url(r'^login/(?P<school>\w+)', views.log_view),
    url(r'^door$', views.door_view),
    url(r'^checkname$', views.check_name),
    url(r'^check_login$', views.check_login),
    url(r'^get_code$', views.send_code),
    url(r'^check_student$', views.check_student),
    url(r'^login_check_name$', views.login_check_name),

]