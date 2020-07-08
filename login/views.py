from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
from index import consumers



def login_(request):
    if request.method =='POST':
        username = request.POST.get('account')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)
            if username not in consumers.ChatConsumer.logined:
                return redirect('/chatting/public')
            else:
                login_fail(request,'该用户已经登录')
        else:
            login_fail(request,'用户名或密码错误')
            return redirect('/login')
    return render(request,'login/login.html')

def login_fail(request,resason):
    messages.success(request, "登陆失败:%s" % resason)

def re_direct(request):
    return redirect('/login')

def logout_(request):
    logout(request)
    return redirect('/login')