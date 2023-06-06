
from django.contrib.auth import  authenticate, login, get_user_model, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import loginform, registerform, changepwd, m_loginform, m_registerform,m_changepwd, prefferences, m_prefferences
from django.contrib.auth import authenticate, login, get_user_model, logout
from .models import invitees
from . import email as ml
from . import gen_text
import os
import string
import random
from . import mobile as m


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
    uval=request.GET.get('uval')
    pval=request.GET.get('pval')
    agent = request.META["HTTP_USER_AGENT"]
    if 'Mobile' in agent:
        
        if get_uname(request)!='Not loged in.':
            logout(request)
            return redirect('home')
            
        else:
            if uval!=None and pval!=None:
                username=uval
                password=pval
                user=authenticate(request,username=username,password=password)
                if user==None:
                    return render(request,'m_landing.html',\
                        {'click_form_login':'Incorrect username or password.',\
                        'display_trigger':'<div style="display:none;">',\
                        'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">',\
                        'form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>',\
                        'uname':get_uname(request)})
                else:
                    login(request,user)
                    return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator('aboutus')})
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                if user==None:
                    return render(request,'m_landing.html',\
                        {'click_form_login':'Incorrect username or password.',\
                        'display_trigger':'<div style="display:none;">',\
                        'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">',\
                        'form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>',\
                        'uname':get_uname(request)})
                else:
                    login(request,user)
                    return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div3':m.mobile_generator('aboutus')})
            return render(request,'m_landing.html',{'click_form_login':m_loginform(),\
                'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">',\
                'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">',\
                'form_wrapper_end':'<tr><th></th><th><button type="submit" class="m_pos_button2">Submit</button></th><td></td></tr></table></form></div>',\
                'uname':get_uname(request)})
    else:
        if get_uname(request)!='Not loged in.':
            logout(request)
            return redirect('home')
            
        else:
            if uval!=None and pval!=None:
                username=uval
                password=pval
                user=authenticate(request,username=username,password=password)
                if user==None:
                    return render(request,'landing.html',{'click_form_login':'Incorrect username or password.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                else:
                    login(request,user)
                    return render(request,'landing_log.html')
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                if user==None:
                    return render(request,'landing.html',{'click_form_login':'Incorrect username or password.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                else:
                    login(request,user)
                    return render(request,'landing_log.html')
            return render(request,'landing.html',{'click_form_login':loginform(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})


def register_view(request):
    form=registerform(request.POST or None)
    p1=id_generator()
    mobile_trig=False
    agent = request.META["HTTP_USER_AGENT"]
    if 'Mobile' in agent:
        mobile_trig=True
    if get_uname(request)=='Not loged in.':
        if mobile_trig:
            return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Please log in to use this section!','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
        else:
            return render(request,'landing.html',{'click_form_login':'Please log in to use this section!','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
    else:
        
        if request.user.is_superuser:
            
            if form.is_valid():
                if request.POST.get("create_user"):
                    username=form.cleaned_data['username']
                    password1=p1
                    if User.objects.filter(username=username).exists():
                        if mobile_trig:
                            return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Username already exists.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                        else:
                            return render(request,'landing_log.html',{'click_form_login':'Username already exists.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                    else:
                        email=form.cleaned_data['email']
                        party_no=int(form.cleaned_data['participants'])
                        get_user_model().objects.create_user(username,email,password1)
                        if party_no>1:
                            for x in range(1, party_no+1):
                                invitees_inst = invitees()            
                                invitees_inst.name = str(username)+' - seat '+str(x)
                                invitees_inst.real_name= str(username)+' - seat '+str(x)
                                invitees_inst.unq_id = str(p1)
                                invitees_inst.table_id = 'Not Assigned'
                                invitees_inst.setting_name = 'Not Assigned'
                                invitees_inst.e_mail = email
                                invitees_inst.menu_prefference='We will eat anything'
                                invitees_inst.Freeform_comments=''
                                invitees_inst.save()
                        else:
                                invitees_inst = invitees()            
                                invitees_inst.name = str(username)
                                invitees_inst.unq_id = str(p1)
                                invitees_inst.table_id = 'Not Assigned'
                                invitees_inst.setting_name = 'Not Assigned'
                                invitees_inst.e_mail = email
                                invitees_inst.real_name= str(username)
                                invitees_inst.menu_prefference='We will eat anything'
                                invitees_inst.Freeform_comments=''
                                invitees_inst.save()
                        if mobile_trig:
                            return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                        else:
                            return render(request,'landing_log.html',{'click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                else:
                    if mobile_trig:
                        return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                    else:
                        return render(request,'landing_log.html',{'click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
            else:
                if request.POST.get("delete_participant"):
                    User.objects.filter(username=str(request.POST.get("delete_participant"))).delete()
                    invitees.objects.filter(name__startswith=str(request.POST.get("delete_participant"))).delete()
                    if mobile_trig:
                        return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                    else:
                        return render(request,'landing_log.html',{'click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                else:
                    if request.POST.get("edit_participant"):
                        query_res=invitees.objects.filter(name__startswith=str(request.POST.get("edit_participant"))).count() 
                        seats_list=[]
                        real_name=[]
                        menu_pref=[]
                        f_comm=[]
                        party=[]
                        for x in invitees.objects.filter(name__startswith=str(request.POST.get("edit_participant"))).all():
                            seats_list.append(str(x.name))
                            real_name.append(str(x.real_name))
                            menu_pref.append(str(x.menu_prefference))
                            f_comm.append(str(x.Freeform_comments))
                            party.append(str(x.particpation))
                                            
                        if mobile_trig:
                            prefferences_inst = m_prefferences(query_res,seat_no=seats_list,r_name=real_name,menu_pref=menu_pref,f_comm=f_comm,party=party)
                            return render(request,'m_landing_log.html',{'click_form_login':prefferences_inst,'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','form_wrapper_start':'<div class="dropbtn66"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th align="right"><button type="submit" name="save_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Submit</button></th><td></td></tr></table></form>','uname':get_uname(request)})     
                        else:
                            prefferences_inst = prefferences(query_res,seat_no=seats_list,r_name=real_name,menu_pref=menu_pref,f_comm=f_comm,party=party)
                            return render(request,'landing_log.html',{'click_form_login':prefferences_inst,'form_wrapper_start':'<div class="dropbtn66"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="save_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Submit</button></th><td></td></tr></table></form>','uname':get_uname(request)})     
                    else:
                        if request.POST.get("save_edit"):
                            query_res=invitees.objects.filter(name__startswith=str(request.POST.get("save_edit"))).count()
                            outval=''

                            for x in range(0,query_res):
                                #Here Seat_x is NONE - WHY?
                                outval=outval+str(request.POST.get("Seat_"+str(x+1)))+'<br>'   
                                invitees.objects.filter(name=str(request.POST.get("Seat_"+str(x+1)))).update(menu_prefference=str(request.POST.get("Menu_prefference_"+str(x+1))),Freeform_comments=str(request.POST.get("Freeform_comments_"+str(x+1))),real_name=str(request.POST.get("Participant_Name_"+str(x+1))),particpation=str(request.POST.get("Participation_"+str(x+1))))    
                            if mobile_trig:
                                return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                            else:
                                return render(request,'landing_log.html',{'click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                        else:
                            if mobile_trig:
                                return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
                            else:
                                return render(request,'landing_log.html',{'click_form_login':registerform(),'form_wrapper_start':'<div class="dropbtn3"><form method="post"><table>','form_wrapper_end':'<tr><th></th><th><button type="submit" name="create_user" value="1" class="pos_button2">Submit</button></th><td></td></tr></table></form><div style ="position: absolute; top: 23vh;"><label><b>Invitees list:</b></label></div><div style="overflow-y: auto; width:90%; bottom: 3vh; position: absolute; top: 25vh;">'+str(gen_text.get_party_full())+'</div></div>','uname':get_uname(request)})
        else:
            if request.POST.get("save_edit"):
                
                query_res=invitees.objects.filter(name__startswith=str(get_uname(request))).count()
                outval=''
      
                for x in range(0,query_res):
                    outval=outval+str(request.POST.get("Seat_"+str(x+1)))+'<br>'
                    #print(str(request.POST.get("Seat_"+str(x+1))))
                    invitees.objects.filter(name=str(request.POST.get("Seat_"+str(x+1)))).update(menu_prefference=str(request.POST.get("Menu_prefference_"+str(x+1))),Freeform_comments=str(request.POST.get("Freeform_comments_"+str(x+1))),real_name=str(request.POST.get("Participant_Name_"+str(x+1))),particpation=str(request.POST.get("Participation_"+str(x+1)))) 
                    print(outval)
                    print(str(request.POST.get("Seat_1")))
                seats_list=[]
                real_name=[]
                menu_pref=[]
                f_comm=[]
                party=[]
                for x in invitees.objects.filter(name__startswith=str(get_uname(request))).all():
                            seats_list.append(str(x.name))
                            real_name.append(str(x.real_name))
                            menu_pref.append(str(x.menu_prefference))
                            f_comm.append(str(x.Freeform_comments))
                            party.append(str(x.particpation))
                            
                
                if mobile_trig:
                    prefferences_inst = m_prefferences(query_res,seat_no=seats_list,r_name=real_name,menu_pref=menu_pref,f_comm=f_comm,party=party)
                    return render(request,'m_landing_log.html',{'click_form_login':prefferences_inst,'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','form_wrapper_start':'<div class="dropbtn66"><form method="post"><table>','form_wrapper_end':'<tr><th><button type="submit" name="pwd_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Change Password</button></th><th align="right"><button type="submit" name="save_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Save</button></th><td></td></tr></table></form>','uname':get_uname(request)})  
                else:
                    prefferences_inst = prefferences(query_res,seat_no=seats_list,r_name=real_name,menu_pref=menu_pref,f_comm=f_comm,party=party)
                    return render(request,'landing_log.html',{'click_form_login':prefferences_inst,'form_wrapper_start':'<div class="dropbtn66"><form method="post"><table>','form_wrapper_end':'<tr><th><button type="submit" name="pwd_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Change Password</button></th><th><button type="submit" name="save_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Save</button></th><td></td></tr></table></form>','uname':get_uname(request)})  
            elif request.POST.get("pwd_edit"):
                return redirect(change_password)
            else:
                        query_res=invitees.objects.filter(name__startswith=str(get_uname(request))).count() 
                        seats_list=[]
                        real_name=[]
                        menu_pref=[]
                        f_comm=[]
                        party=[]
                        for x in invitees.objects.filter(name__startswith=str(get_uname(request))).all():
                            seats_list.append(str(x.name))
                            real_name.append(str(x.real_name))
                            menu_pref.append(str(x.menu_prefference))
                            f_comm.append(str(x.Freeform_comments))
                            party.append(str(x.particpation))
                            print(str(x.particpation))
                        
                        if mobile_trig:
                            prefferences_inst = m_prefferences(query_res,seat_no=seats_list,r_name=real_name,menu_pref=menu_pref,f_comm=f_comm,party=party)
                            return render(request,'m_landing_log.html',{'click_form_login':prefferences_inst,'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','form_wrapper_start':'<div class="dropbtn66"><form method="post"><table>','form_wrapper_end':'<tr><th><button type="submit" name="pwd_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Change Password</button></th><th align="right"><button type="submit" name="save_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Save</button></th><td></td></tr></table></form>','uname':get_uname(request)})  
                        else:
                            prefferences_inst = prefferences(query_res,seat_no=seats_list,r_name=real_name,menu_pref=menu_pref,f_comm=f_comm,party=party)
                            return render(request,'landing_log.html',{'click_form_login':prefferences_inst,'form_wrapper_start':'<div class="dropbtn66"><form method="post"><table>','form_wrapper_end':'<tr><th><button type="submit" name="pwd_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Change Password</button></th><th><button type="submit" name="save_edit" value="'+str(request.POST.get("edit_participant"))+'" class="pos_button2">Save</button></th><td></td></tr></table></form>','uname':get_uname(request)})  
    

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
                    return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Your password has been changed.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                else:
                    return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':'Provided passwords do not match.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})

            return render(request,'m_landing_log.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form_login':m_changepwd(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button_pwd">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})


    else:
        if request.user.is_authenticated:
            u=User.objects.get(username=request.user)
            if form.is_valid():
                p1=form.cleaned_data['password1']
                p2=form.cleaned_data['password2']
                if p1==p2:
                    u.set_password(p1)
                    u.save()
                    return render(request,'landing_log.html',{'click_form_login':'Your password has been changed.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})
                else:
                    return render(request,'landing_log.html',{'click_form_login':'Provided passwords do not match.','form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th></th><td></td></tr></table></form></div>','uname':get_uname(request)})

            return render(request,'landing_log.html',{'click_form_login':changepwd(),'form_wrapper_start':'<div class="dropbtn2"><form method="post"><table style="width:100%">','form_wrapper_end':'<tr><th></th><th><button type="submit" class="pos_button2">Submit</button></th><td></td></tr></table></form></div>','uname':get_uname(request)})

