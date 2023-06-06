"""mariage_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views, seating_admin
from. import identity_management as im


urlpatterns = [
    path('',views.home, name='home'), #ok
    path('mobile',views.m_show_txt, name='mobile'), # - ok
    path('show_txt',views.show_txt, name='show_txt'), #ok
    path('seating_admin',seating_admin.seating_admin_REV, name='seating_admin'), #ok
    path('register', im.register_view, name='register'),#ok
    path('login', im.login_view, name='login'),#ok
    path('logout', im.logout_view, name='logout'),#ok
    path('cpwd', im.change_password, name='cpwd'),#ok 
    path('admin/', admin.site.urls), #admin site remaining active

]
