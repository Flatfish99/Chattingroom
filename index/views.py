from django.shortcuts import render,redirect
from . import consumers
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request,room_name):
    user= request.user
    content={'user': user,'room_name': room_name}
    if(room_name=='public'):
        return render(request,'index/index.html',content)
    elif(room_name=='sports'):
        return render(request, 'index/sports.html', content)
    elif (room_name == 'reading'):
        return render(request, 'index/reading.html', content)
    elif (room_name == 'gaming'):
        return render(request, 'index/gaming.html', content)
    else:
        return render(request, 'index/others.html', content)


def get_userlist(request):
    userlist = consumers.ChatConsumer.userlist


    return JsonResponse(userlist)

def logined_user(request):
    userlist = consumers.ChatConsumer.logined
    return HttpResponse(userlist)
def create_new_room(request):
    if request.method=='GET':
        room_name = request.GET.get('group_name')
        search_name = request.GET.get('search_room')

        if(search_name==None):
            return redirect('/chatting/%s'%room_name)
        elif(search_name=='公共聊天室'):
            return redirect('/chatting/public')
        elif (search_name == '学习'):
            return redirect('/chatting/reading')
        elif (search_name == '运动'):
            return redirect('/chatting/sports')
        elif (search_name == '游戏'):
            return redirect('/chatting/gaming')
        else:
            return redirect('/chatting/%s' % search_name)