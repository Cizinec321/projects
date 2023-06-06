from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .forms import input_form, m_input_form, seating_generator, m_seating_generator, invitees_form,invitees_disp, m_invitees_disp
from .models import in_form, tables, models, invitees,invitees_x_table
from . import identity_management as im
from . import show_text as st
from . import gen_dat
from . import m_gen_text
from . import seating_algo
import re
from django.db.models import Max



global_text=''
menu_trig=False
#OK HERE

def seating_admin_REV(request):
    
    agent = request.META["HTTP_USER_AGENT"]
    mobile_trig=False
    if 'Mobile' in agent:
        mobile_trig=True
    form=seating_generator(request.POST or None)
    invitees_form_inst=invitees_form(request.POST or None)
    if im.get_uname(request)=='Not loged in.':
        if mobile_trig:
            return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Please log in ot use this section!','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>'})
        else:
            return render(request,'landing.html',{'click_form_login':'Please log in ot use this section!','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>'})
    else:
        #IF administrator is logged in
        if request.user.is_superuser:  
            # if something is pressed inside the form
            if request.method=='POST': 
                #if form is valid we can generate a new seating template if not means we can either publish or display an existing template
                if form.is_valid():    
                    #if we pushed the submit button get template name and save it to session cache                
                    if request.POST.get("intial_form"):
                        template=request.POST['template']
                        request.session['template_name'] = template
                        #if data in fields is usable the save to variables and to session cahce, else throw error
                        if  form.cleaned_data['vertical'].isnumeric() and   form.cleaned_data['horizontal'].isnumeric() and  form.cleaned_data['no_seats'].isnumeric():
                            vertical=int(form.cleaned_data['vertical'])
                            horizontal=int(form.cleaned_data['horizontal'])
                            no_seats=int(form.cleaned_data['no_seats'])
                            name=form.cleaned_data['name']
                            request.session['last_vertical'] = vertical
                            request.session['last_horizontal'] = horizontal
                            request.session['last_no_seats'] = no_seats
                        else:
                            if mobile_trig:
                                return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':'<div class="dropbtn2">Unusable values!<br><br>If the form template is empty, pelase fill in the data for a new template.<div>'})  
                            else:
                                return render(request,'seating_app.html',{'seating_generator':'<div class="dropbtn2">Unusable values!<br><br>If the form template is empty, pelase fill in the data for a new template.<div>'})    
                        #if no template name is entered the generate new
                        if template == '':
                            #if a name for new tempalte is entered then check if already extists. If not, create new template, if yes, throw error
                            if name != "":
                                request.session['template_name'] = name
                                if tables.objects.filter(setting_name =name).exists():
                                    if mobile_trig:
                                        return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':'<div class="dropbtn2">Name already exists!<br><br>Please choose another one.<div>'})
                                    else:
                                        return render(request,'seating_app.html',{'seating_generator':'<div class="dropbtn2">Name already exists!<br><br>Please choose another one.<div>'})
                                else:
                                    
                                    for i in range(horizontal):
                                        for z in range(vertical):
                                            tables_inst = tables()            
                                            tables_inst.table_id = str(i+1)+str(z+1)
                                            tables_inst.no_seats = str(no_seats)
                                            tables_inst.setting_name = name
                                            tables_inst.published=0
                                            tables_inst.save()                                
                                    if mobile_trig:
                                        return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_generator(vertical,horizontal,no_seats) })
                                    else:
                                        return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_generator(vertical,horizontal,no_seats) })
                            else:
                                if mobile_trig:
                                    return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':'<div class="dropbtn2">Please enter a valid name!<br><br>I cannot generate a template without a name.<div>'})
                                else:
                                    return render(request,'seating_app.html',{'seating_generator':'<div class="dropbtn2">Please enter a valid name!<br><br>I cannot generate a template without a name.<div>'})
                        #if tempalte name is entered, ignore entered values and open tempalte
                        else:                           
                             
                            max_val=tables.objects.filter(setting_name =name).aggregate(Max('table_id'))
                            max_seats=tables.objects.filter(setting_name =name).aggregate(Max('no_seats'))
                            vertical=int(max_val['table_id__max'][1])
                            horizontal=int(max_val['table_id__max'][0]) 
                            no_seats=int(max_val['no_seats__max'][0]) 
                            request.session['last_vertical'] = vertical
                            request.session['last_horizontal'] = horizontal                            
                            request.session['last_no_seats'] = no_seats
                            if mobile_trig:
                                return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_load() })  
                            else:                            
                                return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_load() })                    
                    else:
                            #Table_home is available once the template ahs been loaded
                            #if a table home button has been pressed, check number of table and load invitees list and total invitees list drop-down
                            if request.POST.get("table_home"):                           
                                table_value=re.search("(\d+)(?!.*\d)",str(request.POST)).group(1)                            
                                request.session['table_value'] = table_value
                                request.session['template_name'] = str(request.session.get('template_name', None))
                                assigned_seats = invitees_x_table.objects.filter(table_id=table_value,setting_name=str(request.session.get('template_name', None))).count()                            
                                data_dict = {'table_id': table_value, 'setting_name': str(request.session.get('template_name', None)),'assigned_seats':assigned_seats}
                                gen_dat.get_party_list(table_value,str(request.session.get('template_name', None)))
                                if mobile_trig:
                                    return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_load(str(request.session.get('template_name', None))),'click_form_login':invitees_form(initial=data_dict),'form_wrapper_start':'<div class="dropbtn_right_mobile_seating"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th><button type="submit" class="pos_button4" name="close_invitees_list" value="1">Close</button></th><th><button type="submit" class="pos_button5" name="save_invitees_list" value="1">Add participant</button></th><td></td></tr></table></form>'+str(gen_dat.get_party_list(table_value,str(request.session.get('template_name', None))))+'</div>'})
                                else:
                                    return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_load(str(request.session.get('template_name', None))),'click_form_login':invitees_form(initial=data_dict),'form_wrapper_start':'<div class="dropbtn_right"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th><button type="submit" class="pos_button3" name="close_invitees_list" value="1">Close</button></th><th><button type="submit" class="pos_button3" name="save_invitees_list" value="1">Add participant</button></th><td></td></tr></table></form>'+str(gen_dat.get_party_list(table_value,str(request.session.get('template_name', None))))+'</div>'})
                            #save_invitees_list is available once the Table_home button has been pressed
                            #if a save_invitees_list button has been pressed, save changes to table and to session cache
                            elif request.POST.get("save_invitees_list"):
                                
                                request.session['table_value'] = str(request.session.get('table_value', None))
                                request.session['template_name'] = str(request.session.get('template_name', None))                                                    
    
                                party=str(invitees_form_inst['name'].value()) 
                                real_party=str(invitees.objects.filter(name=party).aggregate(Max('real_name'))['real_name__max']) 
                                table_value=str(invitees_form_inst['table_id'].value())
                                print(real_party)
                                if invitees_x_table.objects.filter(name=party,setting_name=str(request.session.get('template_name', None))).exists():                              
                                    invitees_x_table.objects.filter(name=party,setting_name=str(request.session.get('template_name', None))).update(table_id=str(request.session.get('table_value', None)))
                                    invitees_x_table.objects.filter(name=party,setting_name=str(request.session.get('template_name', None))).update(setting_name=str(request.session.get('template_name', None)))
                                    invitees_x_table.objects.filter(name=party,setting_name=str(request.session.get('template_name', None))).update(r_name=str(real_party))
                                else:
                                    txi_inst = invitees_x_table()            
                                    txi_inst.name = party
                                    txi_inst.r_name = real_party
                                    txi_inst.table_id = str(request.session.get('table_value', None))
                                    txi_inst.setting_name = str(request.session.get('template_name', None))
                                    txi_inst.save()      
                                if mobile_trig:
                                    return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_load(str(request.session.get('template_name', None)))})
                                else:
                                    return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_load(str(request.session.get('template_name', None)))})
                            #close_invitees_list is available once the Table_home button has been pressed
                            #if a close_invitees_list button has been pressed, close the table edit menu and display tempalte again
                            elif request.POST.get("close_invitees_list"):                           
                                if mobile_trig:
                                    return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_load(str(request.session.get('template_name', None)))}) 
                                else:
                                    return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_load(str(request.session.get('template_name', None)))})            
                       
                #if form is not valid we can either publish or display an existing template
                else:
                    template=request.POST['template']
                    request.session['template_name'] = template  
                    #if a tempalte name is selected                  
                    if template != '':
                        #if we pushed the publish button
                        if request.POST.get("publish_form"):                           
                                template=request.POST['template']
                                request.session['template_name'] = template
                                tables.objects.update(published=0)
                                # we publish the selected form and display confirmation message
                                tables.objects.filter(setting_name=str(template)).update(published=1)
                                if mobile_trig:
                                    return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':'<div class="dropbtn2">Seating plan named '+str(template)+' is now published!<br><br>This template will be visible now to non-admin users.<div>'})
                                else:
                                    return render(request,'seating_app.html',{'seating_generator':'<div class="dropbtn2">Seating plan named '+str(template)+' is now published!<br><br>This template will be visible now to non-admin users.<div>'})
                        else:
                            #if we pushed the publish button, we pushed the submit button and the numeric fields are empty - in this case we display existing template
                            max_val=tables.objects.filter(setting_name =template).aggregate(Max('table_id'))
                            max_seats=tables.objects.filter(setting_name =template).aggregate(Max('no_seats'))
                            vertical=int(max_val['table_id__max'][1])
                            horizontal=int(max_val['table_id__max'][0]) 
                            no_seats=int(max_seats['no_seats__max'][0]) 
                            request.session['last_vertical'] = vertical
                            request.session['last_horizontal'] = horizontal                        
                            request.session['last_no_seats'] = no_seats 
                            if mobile_trig:
                                return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_load(template) })
                            else:                       
                                return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_load(template) })
                    else:
                        if mobile_trig:
                            return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':'<div class="dropbtn2">Invalid form!<div>'})
                        else:
                            return render(request,'seating_app.html',{'seating_generator':'<div class="dropbtn2">Invalid form!<div>'})
            #if nothing is pressed inside the form it means we just display the form
            else:
                if mobile_trig:
                    return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':m_seating_generator(),'form_wrapper_start':'<div class="dropbtnx_mobile"><form method="post"><table style="text-align: left;width:100%">','form_wrapper_end':'<tr><th><button type="submit" class="pos_button2" name="intial_form" value="1"}>Submit</button></th><th style="text-align: right;"><button type="submit" class="pos_button2" name="publish_form" value="1"}>Publish</button></th><td></td></tr></table></form></div>'})
                else:
                    return render(request,'landing_log.html',{'click_form_login':seating_generator(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="text-align: left;width:100%">','form_wrapper_end':'<tr><th><button type="submit" class="pos_button2" name="intial_form" value="1"}>Submit</button></th><th style="text-align: right;"><button type="submit" class="pos_button2" name="publish_form" value="1"}>Publish</button></th><td></td></tr></table></form></div>'})
        #IF non-administrator is logged in - display other stuff 
        else:
            cnt_aval=tables.objects.filter(published =1).count()
            
            if request.POST.get("table_home"):                           
                                table_value=re.search("(\d+)(?!.*\d)",str(request.POST)).group(1)               
                                request.session['table_value'] = table_value
                                request.session['template_name'] = str(request.session.get('template_name', None))
                                assigned_seats = invitees_x_table.objects.filter(table_id=table_value,setting_name=str(request.session.get('template_name', None))).count() 
                                data_dict = {'table_id': table_value, 'setting_name': str(request.session.get('template_name', None)),'assigned_seats':assigned_seats}
                                gen_dat.get_party_list(table_value,str(request.session.get('template_name', None)))
                                #if the user is assigned to one of the tables on which he clicked then display seating arrangement, else display normal setting again
                                if invitees_x_table.objects.filter(table_id=table_value,name__startswith=str(im.get_uname(request)),setting_name=str(request.session.get('template_name', None))).count()>0:
                                    if mobile_trig:
                                        return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_disp(str(request.session.get('template_name', None)),str(im.get_uname(request))),'click_form_login':m_invitees_disp(initial=data_dict),'form_wrapper_start':'<div class="dropbtn_right"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th><button type="submit" class="pos_button3" name="close_invitees_list" value="1">Close</button></th><td></td></tr></table></form>'+str(gen_dat.get_party_list(table_value,str(request.session.get('template_name', None))))+'</div>'})
                                    else:
                                        return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_disp(str(request.session.get('template_name', None)),str(im.get_uname(request))),'click_form_login':invitees_disp(initial=data_dict),'form_wrapper_start':'<div class="dropbtn_right"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th><button type="submit" class="pos_button3" name="close_invitees_list" value="1">Close</button></th><td></td></tr></table></form>'+str(gen_dat.get_party_list(table_value,str(request.session.get('template_name', None))))+'</div>'})
                                else:
                                    if mobile_trig:
                                        return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_disp(str(request.session.get('template_name', None)),str(im.get_uname(request))) })
                                    else:
                                        return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_disp(str(request.session.get('template_name', None)),str(im.get_uname(request))) })
            else:
                cnt_aval=tables.objects.filter(published =1).count()
                #if a table setting has value in published field 1, display it and collour the tables to which user is assigned in red
                if cnt_aval>0:
                    max_val=tables.objects.filter(published =1).aggregate(Max('table_id'))
                    max_seats=tables.objects.filter(published =1).aggregate(Max('no_seats'))
                    template=tables.objects.filter(published =1).first().setting_name
                    vertical=int(max_val['table_id__max'][1])
                    horizontal=int(max_val['table_id__max'][0]) 
                    no_seats=int(max_seats['no_seats__max'][0]) 
                    request.session['last_vertical'] = vertical
                    request.session['last_horizontal'] = horizontal                        
                    request.session['last_no_seats'] = no_seats 
                    request.session['template_name'] = template   
                    if mobile_trig:
                        return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':seating_algo.m_seat_disp(str(template),str(im.get_uname(request))) })
                    else:                                 
                        return render(request,'seating_app.html',{'seating_generator':seating_algo.seat_disp(str(template),str(im.get_uname(request))) })
                else:
                    if mobile_trig:
                        return render(request,'m_seating_app.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','seating_generator':'<div class="dropbtn2">No seating arangement has been published yet.<br><br>Please try again later or contact us.<div>'})
                    else:
                        return render(request,'seating_app.html',{'seating_generator':'<div class="dropbtn2">No seating arangement has been published yet.<br><br>Please try again later or contact us.<div>'})