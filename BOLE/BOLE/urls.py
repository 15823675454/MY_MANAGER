"""Manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^user/', include('user.urls')),
    url(r'^interior/', include('interior.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^123', views.index1),
    url(r'^head.html', views.head_1),
    url(r'^img/head/(?P<img>.+)', views.img_1),
    url(r'^add$', views.add_html),
    url(r'^art$', views.student_art),
    url(r'^calendar', views.calendar_index),
    url(r'undefined', views.notfound),
    url(r'delete/(?P<stu_id>\w+)', views.delete_student),
    url(r'update/(?P<stu_id>\w+)', views.update_student),
    url(r'^setting', views.teac_set_index)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
