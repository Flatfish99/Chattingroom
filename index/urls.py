from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path('^chatting/(?P<room_name>[^/]+)/',views.index),
    path('get_userlist',views.get_userlist),
    path('get_logined_list',views.logined_user),
    path('create_newroom',views.create_new_room),
]
