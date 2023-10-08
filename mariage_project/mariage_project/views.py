from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .forms import loginform,registerform,seating_generator,loginformEN
from django.contrib.auth import authenticate, login, get_user_model, logout
from . import gen_dat
from . import seating_algo
from .models import in_form, tables, models, invitees,invitees_x_table
from django.db.models import Max


def home(request):
        agent = request.META["HTTP_USER_AGENT"]
        #standard form parameters
        register_form=registerform(request.POST or None)
        seating_form=seating_generator(request.POST or None)

        #html parameters
        uval=request.GET.get('uval')
        pval=request.GET.get('pval')
        langval=request.GET.get('lang')

        if langval=='EN':
                #standard EN template parameters
                login_form=loginformEN(request.POST or None)
                form_wrapper_start_def='<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">'
                form_wrapper_end_seat_aloc='<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Change</button></th><td></td></tr></table></form></div>'
                form_wrapper_end_seat_gen='<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1">Send</button></th><td></td></tr></table></form></div>'
                form_wrapper_end_not_log='<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Connect</button></th><td></td></tr></table></form></div>'
                form_wrapper_end_non_su_nobutton='<tr><th></th><th></th><td></td></tr></table></form></div>'
                form_wrapper_end_non_su_wbutton='<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Change</button></th><td></td></tr></table></form></div>'
                registerform_wrapper_start_hidden='<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">'
                registerform_wrapper_start_show='<div class="dropbtn2_show" id="register"><form method="post"  name="login_request"><table style="width:100%">'
                seatingform_wrapper_start_show='<div class="dropbtn2_alt_show" id="seating"><form method="post"  name="seating_request"><table style="width:100%">'
                seatingform_wrapper_start_hide='<div class="dropbtn2" id="seating"><form method="post"  name="seating_request"><table style="width:100%">'
                seatingform_wrapper_start_hide_alt='<div class="dropbtn2_alt" id="seating"><form method="post"  name="seating_request"><table style="width:100%">'
                seatingform_wrapper_start_show_wbutton='<div class="dropbtn2_alt_show" id="seating"><form method="post"><button type="submit" class="pos_button_unload" value="1">Close</button></form>'
                seatingform_wrapper_end_wbutton='<tr><th></th><th><button type="submit" class="pos_button2" name="seating_request" value="1" >Transmite</button><button type="submit" class="pos_button2" name="publish_request" value="1" >Publish</button></th><td></td></tr></table></form></div>'
                seatingform_wrapper_end_nobutton='<tr><th></th><th></th><td></td></tr></table></form></div>'
        else:
                #standard RO template parameters
                login_form=loginform(request.POST or None)
                form_wrapper_start_def='<div class="dropbtn2" id="login"><form method="post"  name="login_request"><table style="width:100%">'
                form_wrapper_end_seat_aloc='<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Schimbă</button></th><td></td></tr></table></form></div>'
                form_wrapper_end_seat_gen='<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1">Transmite</button></th><td></td></tr></table></form></div>'
                form_wrapper_end_not_log='<tr><th></th><th><button type="submit" class="pos_button2" name="login_request" value="1" >Conectare</button></th><td></td></tr></table></form></div>'
                form_wrapper_end_non_su_nobutton='<tr><th></th><th></th><td></td></tr></table></form></div>'
                form_wrapper_end_non_su_wbutton='<tr><th></th><th><button type="submit" class="pos_button2" name="add_participant" value="1">Schimbă</button></th><td></td></tr></table></form></div>'
                registerform_wrapper_start_hidden='<div class="dropbtn2" id="register"><form method="post"  name="login_request"><table style="width:100%">'
                registerform_wrapper_start_show='<div class="dropbtn2_show" id="register"><form method="post"  name="login_request"><table style="width:100%">'
                seatingform_wrapper_start_show='<div class="dropbtn2_alt_show" id="seating"><form method="post"  name="seating_request"><table style="width:100%">'
                seatingform_wrapper_start_hide='<div class="dropbtn2" id="seating"><form method="post"  name="seating_request"><table style="width:100%">'
                seatingform_wrapper_start_hide_alt='<div class="dropbtn2_alt" id="seating"><form method="post"  name="seating_request"><table style="width:100%">'
                seatingform_wrapper_start_show_wbutton='<div class="dropbtn2_alt_show" id="seating"><form method="post"><button type="submit" class="pos_button_unload" value="1">Închide</button></form>'
                seatingform_wrapper_end_wbutton='<tr><th></th><th><button type="submit" class="pos_button2" name="seating_request" value="1" >Transmite</button><button type="submit" class="pos_button2" name="publish_request" value="1" >Publică</button></th><td></td></tr></table></form></div>'
                seatingform_wrapper_end_nobutton='<tr><th></th><th></th><td></td></tr></table></form></div>'








        if uval!=None and pval!=None:
                user=authenticate(request,username=uval,password=pval)
                if user==None:
                       return render(request,'landing.html',{'language':langval,'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_not_log})
                else:
                        login(request,user)
                        if not request.user.is_superuser:
                                output_l_non_su=seating_algo.seat_load_non_su(request.user,langval)
                                seating_table_non_su=output_l_non_su[0]
                                form_list_non_su=output_l_non_su[1] 

                       
 
        if request.POST.get("login_request"):
            if login_form.is_valid():
                username=login_form.cleaned_data['username']
                password=login_form.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                login(request,user)
                if not request.user.is_superuser:
                        output_l_non_su=seating_algo.seat_load_non_su(request.user,langval)
                        seating_table_non_su=output_l_non_su[0]
                        form_list_non_su=output_l_non_su[1] 
                
        if request.POST.get("logout_request"):
              logout(request)
        if request.POST.get("seating_request"):
              template=request.POST['template']
              
              if template!='':
                request.session['template_value'] = template
                output_l=seating_algo.seat_load(template)
                seating_table=output_l[0]
                form_list=output_l[1]
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_aloc,'form_wrapper_end_non_su':form_wrapper_end_non_su_wbutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_table,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show_wbutton,'seatingform_wrapper_end':'</div>'})
                else:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_aloc,'form_wrapper_end_non_su':form_wrapper_end_non_su_wbutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show_wbutton,'seatingform_wrapper_end':'</div>'})
                
              else:
                horizontal=request.POST['horizontal']
                vertical=request.POST['vertical']
                no_seats=request.POST['no_seats']
                name=request.POST['name']
                request.session['template_value'] = name
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
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_aloc,'form_wrapper_end_non_su':form_wrapper_end_non_su_wbutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_table,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show_wbutton,'seatingform_wrapper_end':'</div>'})
                else:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_aloc,'form_wrapper_end_non_su':form_wrapper_end_non_su_wbutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show_wbutton,'seatingform_wrapper_end':'</div>'})
        if request.POST.get("publish_request"):
                template=request.POST['template']    
                tables.objects.update(published=0)
                tables.objects.filter(setting_name=template).update(published=1)
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_form,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_hide,'seatingform_wrapper_end':seatingform_wrapper_end_wbutton})
                else:
                       
                       return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show,'seatingform_wrapper_end':seatingform_wrapper_end_nobutton})
        
                
        if request.POST.get('add_participant'):
                template=request.session.get('template_value', None)
                part_name=request.POST['name']
                table_id=request.POST['table_id']
                real_party=str(invitees.objects.filter(real_name=part_name).aggregate(Max('real_name'))['real_name__max'])  
                ass_cnt=invitees_x_table.objects.filter(r_name=part_name,table_id=table_id).count()   
                if ass_cnt>0:
                        invitees_x_table.objects.filter(r_name=part_name,table_id=table_id).delete()
                else:          
                        txi_inst = invitees_x_table()                           
                        txi_inst.name = part_name
                        txi_inst.r_name = real_party
                        txi_inst.table_id = table_id
                        txi_inst.setting_name = template
                        txi_inst.save() 
                output_l=seating_algo.seat_load(template)
                seating_table=output_l[0]
                form_list=output_l[1]
              
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_aloc,'form_wrapper_end_non_su':form_wrapper_end_non_su_wbutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_table,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show_wbutton,'seatingform_wrapper_end':'</div>'})
                else:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_aloc,'form_wrapper_end_non_su':form_wrapper_end_non_su_wbutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_show_wbutton,'seatingform_wrapper_end':'</div>'})
                
                       
        if request.POST.get('save_participant'):
                p1=gen_dat.id_generator()
                username=request.POST['username']
                email=request.POST['email']
                party_no=int(request.POST['participants'])
                get_user_model().objects.create_user(username,email,p1)
                if party_no>1:
                        for x in range(1, party_no+1):
                                invitees_inst = invitees()            
                                invitees_inst.name = str(username)+' - seat '+str(x)
                                invitees_inst.real_name= str(username)+' - seat '+str(x)
                                invitees_inst.unq_id = str(p1)
                                invitees_inst.table_id = 'Not Assigned'
                                invitees_inst.setting_name = 'Not Assigned'
                                invitees_inst.e_mail = email
                                invitees_inst.menu_prefference='Mănânc orice'
                                invitees_inst.Freeform_comments=''
                                invitees_inst.particpation='Nu'
                                invitees_inst.save()
                else:
                                invitees_inst = invitees()            
                                invitees_inst.name = str(username)
                                invitees_inst.unq_id = str(p1)
                                invitees_inst.table_id = 'Not Assigned'
                                invitees_inst.setting_name = 'Not Assigned'
                                invitees_inst.e_mail = email
                                invitees_inst.real_name= str(username)
                                invitees_inst.menu_prefference='Mănânc orice'
                                invitees_inst.Freeform_comments=''
                                invitees_inst.particpation='Nu'
                                invitees_inst.save()
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_form,'registerform_wrapper_start':registerform_wrapper_start_show,'seatingform_wrapper_start':seatingform_wrapper_start_hide,'seatingform_wrapper_end':seatingform_wrapper_end_wbutton})
                else:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_show,'seatingform_wrapper_start':seatingform_wrapper_start_show,'seatingform_wrapper_end':seatingform_wrapper_end_wbutton})
                
                       
        if request.POST.get("delete_participant"):
                User = get_user_model()
                User.objects.filter(username=str(request.POST.get("delete_participant"))).delete()
                invitees.objects.filter(name__startswith=str(request.POST.get("delete_participant"))).delete()
                invitees_x_table.objects.filter(name__startswith=str(request.POST.get("delete_participant"))).delete()
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_form,'registerform_wrapper_start':registerform_wrapper_start_show,'seatingform_wrapper_start':seatingform_wrapper_start_hide,'seatingform_wrapper_end':seatingform_wrapper_end_wbutton})
                else:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_show,'seatingform_wrapper_start':seatingform_wrapper_start_show,'seatingform_wrapper_end':seatingform_wrapper_end_nobutton})
                
                       

        if request.POST.get("inv_save"):
                if not request.user.is_superuser:
                        output_l_non_su=seating_algo.seat_load_non_su(request.user,langval)
                        seating_table_non_su=output_l_non_su[0]
                        form_list_non_su=output_l_non_su[1]  
                post_data = request.POST
                
                for i in post_data:
                        if str(i).startswith('Seat_'):                               
                               invitee=post_data[i]
                               num=int(str(i).replace('Seat_',''))
                               print(post_data['Email_Adrress_'+str(num)])
                               invitees.objects.filter(name=invitee).update(real_name=post_data['Participant_Name_'+str(num)],particpation=post_data['Participation_'+str(num)],e_mail=post_data['Email_Adrress_'+str(num)],menu_prefference=post_data['Menu_prefference_'+str(num)],Freeform_comments=post_data['Freeform_comments_'+str(num)])
                               
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_form,'registerform_wrapper_start':registerform_wrapper_start_show,'seatingform_wrapper_start':seatingform_wrapper_start_hide,'seatingform_wrapper_end':seatingform_wrapper_end_wbutton})
                else:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_show,'seatingform_wrapper_start':seatingform_wrapper_start_hide_alt,'seatingform_wrapper_end':seatingform_wrapper_end_nobutton})
                
        if request.user.is_authenticated:
                if request.user.is_superuser:
                        return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_form_register':register_form,'click_ee_list':gen_dat.get_party_full(),'click_form_seating':seating_form,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_hide,'seatingform_wrapper_end':seatingform_wrapper_end_wbutton})
                else:
                       
                       return render(request,'landing_log.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'seat_handling_form':form_list_non_su,'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load_non_su(request.user,langval),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_seat_gen,'form_wrapper_end_non_su':form_wrapper_end_non_su_nobutton,'click_ee_list':gen_dat.get_party_full_non_su(request.user,langval),'click_form_seating':seating_table_non_su,'registerform_wrapper_start':registerform_wrapper_start_hidden,'seatingform_wrapper_start':seatingform_wrapper_start_hide_alt,'seatingform_wrapper_end':seatingform_wrapper_end_nobutton})
        
                       
        else:
                return render(request,'landing.html',{'language':langval,'click_check_div3':gen_dat.gen_text(langval),'click_form_login':login_form,'invitees_handling_form':gen_dat.details_load(),'form_wrapper_start':form_wrapper_start_def,'form_wrapper_end':form_wrapper_end_not_log})
