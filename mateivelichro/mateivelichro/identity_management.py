
from django.contrib.auth import  authenticate, login, get_user_model, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import loginform, registerform, changepwd, m_loginform, m_registerform,m_changepwd
from django.contrib.auth import authenticate, login, get_user_model, logout
from . import email as ml
import os
import string
import random


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_uname(request):

    if request.user.is_authenticated:
        uname=request.user
    else:
        uname='Not loged in.'
    return uname

def logout_view(request):
    logout(request)
    return redirect('home')



def login_view(request):
    form=loginform(request.POST or None)
    agent = request.META["HTTP_USER_AGENT"]
    if 'Mobile' in agent:
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user==None:
                return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Incorrect username or password.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
            login(request,user)
        return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':m_loginform(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})


    else:

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user==None:
                return render(request,'landing.html',{'click_form_login':'Incorrect username or password.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
            login(request,user)
        return render(request,'landing.html',{'click_form_login':loginform(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})


def register_view(request):
    form=registerform(request.POST or None)
    p1=id_generator()
    agent = request.META["HTTP_USER_AGENT"]
    if 'Mobile' in agent:
        if form.is_valid():
            username=form.cleaned_data['username']
            password1=p1
            if User.objects.filter(username=username).exists():
                return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Username already exists.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
            else:
                email=form.cleaned_data['email']
                get_user_model().objects.create_user(username,email,password1)
                ml.send_email(str(email),p1,username)
                return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'An e-mail with a generated password has ben sent to you.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})


        return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':m_registerform(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})

    else:
        if form.is_valid():
            username=form.cleaned_data['username']
            password1=p1
            if User.objects.filter(username=username).exists():
                return render(request,'landing.html',{'click_form_login':'Username already exists.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
            else:
                email=form.cleaned_data['email']
                get_user_model().objects.create_user(username,email,password1)
                ml.send_email(str(email),p1,username)
                return render(request,'landing.html',{'click_form_login':'An e-mail with a generated password has ben sent to you.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})


        return render(request,'landing.html',{'click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})

def change_password(request):
    form=changepwd(request.POST or None)
    agent = request.META["HTTP_USER_AGENT"]
    if 'Mobile' in agent:
        if request.user.is_authenticated:
            u=User.objects.get(username=request.user)
            if form.is_valid():
                p1=form.cleaned_data['password1']
                p2=form.cleaned_data['password2']
                if p1==p2:
                    u.set_password(p1)
                    u.save()
                    return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Your password has been changed.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                else:
                    return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Provided passwords do not match.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})

        return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':m_changepwd(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})


    else:
        if request.user.is_authenticated:
            u=User.objects.get(username=request.user)
            if form.is_valid():
                p1=form.cleaned_data['password1']
                p2=form.cleaned_data['password2']
                if p1==p2:
                    u.set_password(p1)
                    u.save()
                    return render(request,'landing.html',{'click_form_login':'Your password has been changed.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                else:
                    return render(request,'landing.html',{'click_form_login':'Provided passwords do not match.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})

        return render(request,'landing.html',{'click_form_login':changepwd(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})

