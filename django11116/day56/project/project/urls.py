"""project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse, render


# request是来自client的res信息，作为参数接收
def index(request):
    return HttpResponse("123")


# 找到html页面——读取文件——按照HTTP协议回复
def login(request):
    return render(request, 'login.html')


def resolveLogin(request):
    post = request.POST
    # 打印出的post形态如下：
    # <QueryDict: {'username': ['123'], 'password': ['123']}>
    # 所以其中的信息可以通过字典取
    username = post.get('username')
    password = post.get('password') # get 可以防止报错，找不到有默认值

    # 应该向数据库找的判断
    if username == '123' and password == '123':
        return HttpResponse("T")
    else:
        return HttpResponse("F")


# 这个list记录所有关于url的目标进入函数
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^login/', login),
    url(r'^post-login', resolveLogin)
]
