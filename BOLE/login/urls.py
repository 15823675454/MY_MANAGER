from django.conf.urls import url
from . import views
# 路径：login/urls
urlpatterns = [
    url(r'^$', views.login_index)

]