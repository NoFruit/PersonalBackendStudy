from django.shortcuts import render
from app01.models import UserInfo

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库检索
        ret = UserInfo.objects.filter(username=username, password=password)
        if ret:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})

    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')