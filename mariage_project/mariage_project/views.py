from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .forms import loginform,registerform,seating_generator,invitees_form
from django.contrib.auth import authenticate, login, get_user_model, logout
from . import identity_management as im
from . import show_text as st
from . import gen_dat
from . import mobile as m
from . import seating_algo
from .models import in_form, tables, models, invitees,invitees_x_table
from django.db.models import Max

#OK HERE
def home(request):
    print('entered home')
    agent = request.META["HTTP_USER_AGENT"]
    login_form=loginform(request.POST or None)
    register_form=registerform(request.POST or None)
    seating_form=seating_generator(request.POST or None)
    invitees_form_inst=invitees_form(request.POST or None) # Don't know what this is. Need to check it out
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
        if request.POST.get("seating_request"):
              template=request.POST['template']
              
              if template!='':
                request.session['template_value'] = template
                output_l=seating_algo.seat_load(template)
                seating_table=output_l[0]
                form_list=output_l[1]
                return render(request,'landing_log.html',{'click_check_div3':gen_dat.gen_text(),'seat_handling_form':form_list,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Add</button></th><td></td></tr></table></form></div>','click_form_register':register_form,'click_form_seating':seating_table,'registerform_wrapper_start':'<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">','registerform_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>','seatingform_wrapper_start':'<div class="dropbtn2_alt_show" id="seating"><form method="post"><button type="submit" class="pos_button_unload" value="1">Unload</button></form>','seatingform_wrapper_end':'</div>'})
                
              else:
                horizontal=request.POST['horizontal']
                vertical=request.POST['vertical']
                no_seats=request.POST['no_seats']
                name=request.POST['name']
                for i in range(int(horizontal)):
                        for z in range(int(vertical)):
                                tables_inst = tables()            
                                tables_inst.table_id = str(i+1)+str(z+1)
                                tables_inst.no_seats = str(no_seats)
                                tables_inst.setting_name = name
                                tables_inst.published=0
                                tables_inst.save()   
                output_l=seating_algo.seat_load(name)
                seating_table=output_l[0]
                form_list=output_l[1]
                return render(request,'landing_log.html',{'click_check_div3':gen_dat.gen_text(),'seat_handling_form':form_list,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Add</button></th><td></td></tr></table></form></div>','click_form_register':register_form,'click_form_seating':seating_table,'registerform_wrapper_start':'<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">','registerform_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>','seatingform_wrapper_start':'<div class="dropbtn2_alt_show" id="seating"><form method="post"><button type="submit" class="pos_button_unload" value="1">Unload</button></form>','seatingform_wrapper_end':'</div>'})
                  
                
        if request.POST.get('add_participant'):
                template=request.session.get('template_value', None)
                part_name=request.POST['name']
                table_id=request.POST['table_id']
                real_party=str(invitees.objects.filter(name=part_name).aggregate(Max('real_name'))['real_name__max'])                 
                txi_inst = invitees_x_table()            
                txi_inst.name = part_name
                txi_inst.r_name = real_party
                txi_inst.table_id = table_id
                txi_inst.setting_name = template
                txi_inst.save() 
                output_l=seating_algo.seat_load(template)
                seating_table=output_l[0]
                form_list=output_l[1]
              
           
                return render(request,'landing_log.html',{'click_check_div3':gen_dat.gen_text(),'seat_handling_form':form_list,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Add</button></th><td></td></tr></table></form></div>','click_form_register':register_form,'click_form_seating':seating_table,'registerform_wrapper_start':'<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">','registerform_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>','seatingform_wrapper_start':'<div class="dropbtn2_alt_show" id="seating"><form method="post"><button type="submit" class="pos_button_unload" value="1">Unload</button></form>','seatingform_wrapper_end':'</div>'})
                
        if request.user.is_authenticated:
                return render(request,'landing_log.html',{'click_check_div3':gen_dat.gen_text(),'click_form_login':login_form,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1">Submit</button></th><td></td></tr></table></form></div>','click_form_register':register_form,'click_form_seating':seating_form,'registerform_wrapper_start':'<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">','registerform_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>','seatingform_wrapper_start':'<div class="dropbtn2" id="seating"><form method="post"  name="seating_request"><table style="width:100%">','seatingform_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="seating_request" value="1" >Submit</button></th><td></td></tr></table></form></div>'})

        else:
                return render(request,'landing.html',{'click_check_div3':gen_dat.gen_text(),'click_form_login':login_form,'form_wrapper_start':'<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Submit</button></th><td></td></tr></table></form></div>'})

 