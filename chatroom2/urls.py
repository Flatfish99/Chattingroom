"""chatroom2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import urls as login_urls
from register import urls as register_urls
from index import urls as index_urls
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(login_urls)),
    path('', include(register_urls)),
    path('', include(index_urls)),
    path('', views.re_direct),

]
