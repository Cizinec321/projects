from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from .forms import loginform,registerform
from django.contrib.auth import authenticate, login, get_user_model, logout
from . import identity_management as im
from . import show_text as st
from . import gen_dat
from . import mobile as m



#OK HERE
def home(request):
    print('entered home')
    agent = request.META["HTTP_USER_AGENT"]
    login_form=loginform(request.POST or None)
    register_form=registerform(request.POST or None)
    if 'Mobile' in agent:
        print('mobile')
        if im.get_uname(request)=='Not loged in.':
                return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator('aboutus')})
        else:
                return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator('aboutus')})
    else:
        if request.POST.get("login_request"):
            if login_form.is_valid():
                username=login_form.cleaned_data['username']
                password=login_form.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                login(request,user)
        if request.POST.get("logout_request"):
              logout(request)
        if request.user.is_authenticated:
                return render(request,'landing_log.html',{'click_check_div3':gen_dat.gen_text(),'click_form_login':login_form,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1">Submit</button></th><td></td></tr></table></form></div>','click_form_register':register_form,'registerform_wrapper_start':'<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">','registerform_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>'})

        else:
                return render(request,'landing.html',{'click_check_div3':gen_dat.gen_text(),'click_form_login':login_form,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>'})

