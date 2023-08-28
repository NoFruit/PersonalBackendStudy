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
from django.shortcuts import HttpResponse, render, redirect


# request是来自client的res信息，作为参数接收
def index(request):
    return render(request, 'index.html')


# 找到html页面——读取文件——按照HTTP协议回复
def login(request):
    error_msg = ''
    # 如果POST请求，则说明要处理login逻辑
    if request.method == 'POST':
        post = request.POST
        # 打印出的post形态如下：
        # <QueryDict: {'username': ['123'], 'password': ['123']}>
        # 所以其中的信息可以通过字典取
        username = post.get('username')
        password = post.get('password') # get 可以防止报错，找不到有默认值

        # 应该向数据库找的判断
        if username == '123' and password == '123':
            # return HttpResponse("T")
            return redirect('/index/')  # 重定向至新网页
        else:
            # return HttpResponse("F")
            # 字典参数可以用于替换html中{{}}符号的特定文本
            # return render(request, 'login.html', {'error_msg':'用户名密码错误'})
            error_msg = '用户名密码错误'

    # 如果不是post请求，说明是刚来请求login页面的
    # 优化到通过变量error_msg来传输错误信息
    return render(request, 'login.html', {'error_msg':error_msg})


# def resolveLogin(request):
#     post = request.POST
#     # 打印出的post形态如下：
#     # <QueryDict: {'username': ['123'], 'password': ['123']}>
#     # 所以其中的信息可以通过字典取
#     username = post.get('username')
#     password = post.get('password') # get 可以防止报错，找不到有默认值

#     # 应该向数据库找的判断
#     if username == '123' and password == '123':
#         # return HttpResponse("T")
#         return redirect('/index/')  # 重定向至新网页
#     else:
#         return HttpResponse("F")


# 这个list记录所有关于url的目标进入函数
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^login/', login)
    # url(r'^resolveLogin', resolveLogin)
]
