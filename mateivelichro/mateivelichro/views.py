from django.shortcuts import render
from .forms import input_form, m_input_form
from .models import in_form
from . import identity_management as im
from . import show_text as st
from . import gen_text
from . import m_gen_text
# Create your views here.

global_text=''
menu_trig=False
#DEFINE GLOBAL VARIABLE WHICH REMEMBERS IF DROPDOWN MENU IS ACTIVE AND USE IT TO SWITCH ACTIVE/INACTIVE
def home(request):
    agent = request.META["HTTP_USER_AGENT"]

    if 'Mobile' in agent:
        return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div2':'','click_check_div3':m_gen_text.gen_text('about'),'form_wrapper_start':'','form_wrapper_end':'','uname':im.get_uname(request),'PLM':agent})
    else:
        return render(request,'landing.html',{'click_check':'main load','uname':im.get_uname(request)})

def show_txt(request):
    global global_text
    #global menu_trig
    agent = request.META["HTTP_USER_AGENT"]

    if 'Mobile' in agent:
        text= st.gen_text(request.GET['pass'])     
        global_text=text        
        return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_check_div2':'','click_check_div3':m_gen_text.gen_text(text),'form_wrapper_start':'','form_wrapper_end':'','uname':im.get_uname(request),'PLM':agent})
            
    else:
        text= st.gen_text(request.GET['pass'])
        return render(request,'landing.html',{'click_check_div2':'','click_check_div3':gen_text.gen_text(text),'form_wrapper_start':'','form_wrapper_end':'','uname':im.get_uname(request),'PLM':agent})


def show_form(request):
    global global_text
    #global menu_trig - not used anymore - this was BS
    agent = request.META["HTTP_USER_AGENT"]

    if 'Mobile' in agent:
    # MOBILE
        if request.method=='POST':
            if 'post_comment' in request.POST:
                form=input_form(request.POST)
                
                if form.is_valid():
                    UN_IN=im.get_uname(request)
                    HAP_IN=form.cleaned_data['HAP']



                    data_ins=in_form(UN_DB=UN_IN,HAP_DB=HAP_IN)
                    data_ins.save()
                    print('Data saved')
                else:
                    print("Data not saved")
            else:
                button_name = str(request.POST).replace("<QueryDict: {'",'').replace("': ['']}>",'')
                in_form.objects.filter(id=button_name).delete()        
        if request.user.is_authenticated: 
            outval1=''  
            outval2='' 
            query_res=in_form.objects.all()


            for e in query_res:
                if e.UN_DB==str(im.get_uname(request)):
                    outval1=outval1+'<div class="name_review"><b>'+e.UN_DB+' says:</b></div><br><div class="comm_par-style" id="chd_trig">'+'<br><span>'+e.HAP_DB+'</span><form method="post"><button type="submit" name="'+str(e).replace('in_form object (','').replace(')','')+'" class="del_button" title="Delete"></button></form></div><br><br><br><br>'
                if e.UN_DB!=str(im.get_uname(request)):
                    outval2=outval2+'<div class="name_review"><b>'+e.UN_DB+' says:</b></div><br><div class="comm_par-style">'+'<br><span>'+e.HAP_DB+'</span></div><br><br><br><br>'

            
            global_text=''
            menu_trig=False
            return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form':m_input_form(initial={'UN': im.get_uname(request)}),'click_check_div3': '<div style="position: absolute;top: 100px;bottom:50%;overflow-y: scroll;width:90%; left:5%;overflow-wrap:anywhere;">'+outval1+outval2+'</div>','form_wrapper_start':'<form method="post">','form_wrapper_end':'<br><br><button type="submit" name="post_comment" class="pos_button">Post</button></form>','uname':im.get_uname(request),'PLM':'PLM1'})#<br><br><button type="submit" style="left:5%;position:relative;">Submit</button></form>'})
        else:
            
            query_res=in_form.objects.all()
            outval=''
            for e in query_res:
                outval=outval+'<div class="name_review"><b>'+e.UN_DB+' says:</b></div><br><div class="comm_par-style">'+'<br><span>'+e.HAP_DB+'</span></div><br><br><br><br>'
            global_text=''
            menu_trig=False
            return render(request,'m_landing.html',{'display_trigger':'<div id="menubtn" class="dropdown-content" style="display:none">','click_form':m_input_form(initial={'UN': im.get_uname(request)}),'click_check_div3': '<div style="position: absolute;top: 100px;bottom:50%;overflow-y: scroll;width:90%; left:5%;overflow-wrap:anywhere;">'+outval+'</div>','form_wrapper_start':'<form method="post">','form_wrapper_end':'<br><br><button type="submit" name="post_comment" class="pos_button" disabled title="Log in first">Please log In first</button></form>','uname':im.get_uname(request),'PLM':'PLM1'})#<br><br><button type="submit" style="left:5%;position:relative;">Submit</button></form>'})
#DONE MOBILE

# NON MOBILE
    else:
        if request.method=='POST':
            if 'post_comment' in request.POST:
                form=input_form(request.POST)
                
                if form.is_valid():
                    UN_IN=im.get_uname(request)
                    HAP_IN=form.cleaned_data['HAP']



                    data_ins=in_form(UN_DB=UN_IN,HAP_DB=HAP_IN)
                    data_ins.save()
                    print('Data saved')
                else:
                    print("Data not saved")
            else:
                button_name = str(request.POST).replace("<QueryDict: {'",'').replace("': ['']}>",'')
                in_form.objects.filter(id=button_name).delete()

        
        if request.user.is_authenticated: 
            outval1=''  
            outval2='' 
            query_res=in_form.objects.all()


            for e in query_res:
                if e.UN_DB==str(im.get_uname(request)):
                    outval1=outval1+'<div class="name_review"><b>'+e.UN_DB+' says:</b></div><br><div class="comm_par-style" id="chd_trig">'+'<br><span>'+e.HAP_DB+'</span><form method="post"><button type="submit" name="'+str(e).replace('in_form object (','').replace(')','')+'" class="del_button" title="Delete"></button></form></div><br><br><br><br>'
                if e.UN_DB!=str(im.get_uname(request)):
                    outval2=outval2+'<div class="name_review"><b>'+e.UN_DB+' says:</b></div><br><div class="comm_par-style">'+'<br><span>'+e.HAP_DB+'</span></div><br><br><br><br>'

            
        
            return render(request,'landing.html',{'click_form':input_form(initial={'UN': im.get_uname(request)}),'click_check_div3': outval1+outval2,'form_wrapper_start':'<form method="post">','form_wrapper_end':'<br><br><button type="submit" name="post_comment" class="pos_button">Post</button></form>','uname':im.get_uname(request),'PLM':'PLM1'})#<br><br><button type="submit" style="left:5%;position:relative;">Submit</button></form>'})
        else:
            
            query_res=in_form.objects.all()
            outval=''
            for e in query_res:
                outval=outval+'<div class="name_review"><b>'+e.UN_DB+' says:</b></div><br><div class="comm_par-style">'+'<br><span>'+e.HAP_DB+'</span></div><br><br><br><br>'
            return render(request,'landing.html',{'click_form':input_form(initial={'UN': im.get_uname(request)}),'click_check_div3': outval,'form_wrapper_start':'<form method="post">','form_wrapper_end':'<br><br><button type="submit" name="post_comment" class="pos_button" disabled title="Log in first">Post</button></form>','uname':im.get_uname(request),'PLM':'PLM1'})#<br><br><button type="submit" style="left:5%;position:relative;">Submit</button></form>'})