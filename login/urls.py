from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_),
    path('logout/',views.logout_),

]
