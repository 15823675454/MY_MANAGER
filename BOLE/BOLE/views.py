from django.http import *
from django.shortcuts import render
# project/views


def index(request):

    return render(request, '主页.html')


def index1(request):
    return render(request, 'index.html')


def head_1(request):
    return render(request, 'head.html')


def img_1(request, img):
    with open('../static/img/head/'+img, 'rb') as f:
        data = f.read()
    return render(request, 'static/img/head'+img)




