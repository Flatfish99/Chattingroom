from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators import csrf
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('account')
        password = request.POST.get('password')
        password2 = request.POST.get('password_repeat')
        email= request.POST.get('email')
        print(username,password)
        condition2 = register_check_pswd(request, password, password2)
        if (condition2):
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                register_success(request)
                return redirect('/login')

            except:
                messages.success(request, "注册失败！该用户名已被注册或密码不符合要求")

    return render(request,'register/register.html')
def register_success(request):
    messages.success(request, "注册成功！")

def register_check_pswd(request,pswd1,pswd2):
    if(pswd1!=pswd2):
        messages.success(request, "注册失败！两次输入的密码不一致！")

        return False
    elif(len(pswd1)<=6):
        messages.success(request, "注册失败！密码长度不得小于6位！")
        return False
    else:
        return True

