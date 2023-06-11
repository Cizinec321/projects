from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from .forms import input_form, m_input_form, seating_generator, invitees_form,invitees_disp,loginform
from .models import in_form, tables, models, invitees,invitees_x_table
from . import identity_management as im
from . import show_text as st
from . import gen_dat
from . import mobile as m
from . import seating_algo
import re
from django.db.models import Max


global_text=''
menu_trig=False
#OK HERE
def home(request):
    
    agent = request.META["HTTP_USER_AGENT"]
    global global_text
    global menu_trig
    if 'Mobile' in agent:
        if im.get_uname(request)=='Not loged in.':
                return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator('aboutus')})
        else:
                return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator('aboutus')})
    else:
        if im.get_uname(request)=='Not loged in.':
                #move form wrapers to template!!!!!
                return render(request,'landing.html',{'click_check_div3':gen_dat.gen_text(),'click_form_login':loginform(),'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>',})
        else:
                return render(request,'landing_log.html',{'click_check_div3':gen_dat.gen_text(),'click_form_login':loginform(),'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>',})
#OK HERE
def show_txt(request):
    global global_text
    global menu_trig
    agent = request.META["HTTP_USER_AGENT"]
    if im.get_uname(request)=='Not loged in.':
            return render(request,'landing.html',\
                {'click_check_div2':'',\
                'click_check_div3':gen_dat.gen_text(st.gen_text(request.GET['pass'])),\
                'form_wrapper_start':'',\
                'form_wrapper_end':'',\
                'uname':im.get_uname(request)})
    
    else:
            return render(request,'landing_log.html',\
                {'click_check_div2':'',\
                'click_check_div3':gen_dat.gen_text(st.gen_text(request.GET['pass'])),\
                'form_wrapper_start':'',\
                'form_wrapper_end':'',\
                'uname':im.get_uname(request),})

def m_show_txt(request):
            if im.get_uname(request)=='Not loged in.':
                return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator(request.GET['pass'])})
            else:
                return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator(request.GET['pass'])})

    

