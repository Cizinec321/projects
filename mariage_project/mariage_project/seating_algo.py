
from django.contrib.auth import  authenticate, login, get_user_model, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import loginform, registerform, changepwd, m_loginform, m_registerform,m_changepwd,invitees_form
from django.db.models import Max
from django.contrib.auth import authenticate, login, get_user_model, logout
from . import email as ml
from .models import tables,invitees_x_table
import os
import string
import random


def seat_generator(topbottom, leftright, seat_per_table):

    height=100/(topbottom)
    widht=70/leftright
    left=0
    top=0
    out_html=''
    if height<widht:
        circleh=height
    else:
        circleh=widht
       
    
    for i in range(leftright):

        top=0
        for z in range(topbottom):
            
            out_html=out_html+'<div style=" align-items: center;position: absolute;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;top:'+str(top)+'vh;left:'+str(left)+'vw;"><span class="table_noselect" style="top:5px;align-items: center;height: '+str(circleh)+'vh; width: '+str(circleh)+'vh; border-radius: 50%; display: inline-block;position: relative"><form method="post" style="position: absolute;align-items: center;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;"><button type="submit" name="table_home" value="1" style="background-color: blue;top:'+str((circleh/2)-(circleh/5))+ 'vh;color: white;border: none;border-radius: 70%;position: relative;padding:'+str(circleh/10)+'vh;font-size: 16px;"><input type="hidden" name="id_table" required="" id="id_table" value="'+str(i+1)+str(z+1)+'">'+str(i+1)+str(z+1)+'</button></form></span></div>'
            top=top+height
        left=left+widht
        

    return out_html



def seat_load(name):

    query=tables.objects.filter(setting_name =name) 
    max_val=tables.objects.filter(setting_name =name).aggregate(Max('table_id'))
    
    max_h=int(max_val['table_id__max'][1])
    max_v=int(max_val['table_id__max'][0])  
    height=100/(max_h)
    widht=70/max_v
    left=0
    top=0
    out_html=''
    form_list=[]
    but_count=0
    for items in query:
          
        if height<widht:
            circleh=height
        else:
            circleh=widht
        
        
        for i in range(max_v):

            top=0
            for z in range(max_h): 
                data_dict = {'table_id': (str(i+1)+str(z+1)), 'setting_name': name,'assigned_seats':invitees_x_table.objects.filter(table_id=(str(i+1)+str(z+1)),setting_name=name).count()}                          
                form_list.append(invitees_form(initial=data_dict))
                out_html=out_html+'<div style="align-items: center;position: absolute;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;top:'+str(top)+'vh;left:'+str(left)+'vw;"><span class="table_noselect" style="top:5px;align-items: center;height: '+str(circleh)+'vh; width: '+str(circleh)+'vh; border-radius: 50%; display: inline-block;position: relative"><form method="post" style="position: absolute;align-items: center;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;"><button type="button" name="table_home" value="1" style="background-color: blue;top:'+str((circleh/2)-(circleh/5))+ 'vh;color: white;border: none;border-radius: 70%;position: relative;padding:'+str(circleh/10)+'vh;font-size: 16px;" onclick=document.getElementById('+chr(39)+str(but_count)+chr(39)+').className='+chr(39)+'dropbtn2_show'+chr(39)+'>'+str(i+1)+str(z+1)+'</button></form></span></div>'
                top=top+height
                but_count=but_count+1
            left=left+widht

        return out_html,form_list

def seat_disp(zname,uname):

    query=tables.objects.filter(setting_name =zname) 
    max_val=tables.objects.filter(setting_name =zname).aggregate(Max('table_id'))
    tbl_list=invitees_x_table.objects.filter(setting_name =zname,name__startswith=uname).values_list('table_id', flat=True)
    
    max_h=int(max_val['table_id__max'][1])
    max_v=int(max_val['table_id__max'][0])  
    height=100/(max_h)
    widht=70/max_v
    left=0
    top=0
    out_html=''
    for items in query:
          
        if height<widht:
            circleh=height
        else:
            circleh=widht
        
        
        for i in range(max_v):

            top=0
            for z in range(max_h):
                if str(i+1)+str(z+1) in tbl_list:
                    
                    clr='red'
                else:
                    clr='blue'
                out_html=out_html+'<div style="align-items: center;position: absolute;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;top:'+str(top)+'vh;left:'+str(left)+'vw;"><span class="table_noselect"  style="top:5px;align-items: center;height: '+str(circleh)+'vh; width: '+str(circleh)+'vh;  border-radius: 50%; display: inline-block;position: relative"><form method="post" style="position: absolute;align-items: center;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;"><button type="submit" name="table_home" value="1" style="background-color: '+clr+';top:'+str((circleh/2)-(circleh/5))+ 'vh;color: white;border: none;border-radius: 70%;position: relative;padding:'+str(circleh/10)+'vh;font-size: 16px;"><input type="hidden" name="id_table" required="" id="id_table" value="'+str(i+1)+str(z+1)+'">'+str(i+1)+str(z+1)+'</button></form></span></div>'
                top=top+height
            left=left+widht
        

        return out_html
 
 

def m_seat_disp(zname,uname):

    query=tables.objects.filter(setting_name =zname) 
    max_val=tables.objects.filter(setting_name =zname).aggregate(Max('table_id'))
    tbl_list=invitees_x_table.objects.filter(setting_name =zname,name__startswith=uname).values_list('table_id', flat=True)
    
    max_h=int(max_val['table_id__max'][1])
    max_v=int(max_val['table_id__max'][0])  
    height=100/(max_h)
    widht=70/max_v
    left=0
    top=0
    out_html=''
    for items in query:
          
        if height<widht:
            circleh=height
        else:
            circleh=widht
        
        
        for i in range(max_v):

            top=0
            for z in range(max_h):
                if str(i+1)+str(z+1) in tbl_list:
                    
                    clr='red'
                else:
                    clr='black'
                out_html=out_html+'<div style="align-items: center;position: absolute;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;top:'+str(top)+'vh;left:'+str(left+(left*0.1))+'vh;"><span class="table_noselect" style="top:5px;align-items: center;height: '+str(circleh)+'vh; width: '+str(circleh)+'vh; border-radius: 50%; display: inline-block;position: relative"><form method="post" style="position: absolute;align-items: center;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;"><button type="submit" name="table_home" value="1" style="background-color: '+clr+';top:'+str((circleh/2)-(circleh/5))+ 'vh;color: white;border: none;border-radius: 70%;position: relative;padding:'+str(circleh/10)+'vh;font-size: 16px;"><input type="hidden" name="id_table" required="" id="id_table" value="'+str(i+1)+str(z+1)+'">'+str(i+1)+str(z+1)+'</button></form></span></div>'
                top=top+height
            left=left+widht
        

        return out_html
 

 
def m_seat_generator(topbottom, leftright, seat_per_table):

    height=100/(topbottom)
    widht=70/leftright
    left=0
    top=0
    out_html=''
    if height<widht:
        circleh=height
    else:
        circleh=widht
       
    
    for i in range(leftright):

        top=0
        for z in range(topbottom):

            out_html=out_html+'<div style=" align-items: center;position: absolute;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;top:'+str(top)+'vh;left:'+str(left+(left*0.1))+'vh;"><span class="table_noselect" style="top:5px;align-items: center;height: '+str(circleh)+'vh; width: '+str(circleh)+'vh; border-radius: 50%; display: inline-block;position: relative"><form method="post" style="position: absolute;align-items: center;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;"><button type="submit" name="table_home" value="1" style="background-color: blue;   top:'+str((circleh/2)-(circleh/5))+ 'vh;color: white;border: none;border-radius: 70%;position: relative;padding:'+str(circleh/10)+'vh;font-size: 16px;"><input type="hidden" name="id_table" required="" id="id_table" value="'+str(i+1)+str(z+1)+'">'+str(i+1)+str(z+1)+'</button></form></span></div>'
            top=top+height
        left=left+widht
        

    return out_html


def m_seat_load(name):

    query=tables.objects.filter(setting_name =name) 
    max_val=tables.objects.filter(setting_name =name).aggregate(Max('table_id'))
    
    max_h=int(max_val['table_id__max'][1])
    max_v=int(max_val['table_id__max'][0])  
    height=100/(max_h)
    widht=70/max_v
    left=0
    top=0
    out_html=''
    for items in query:
          
        if height<widht:
            circleh=height
        else:
            circleh=widht
        
        
        for i in range(max_v):

            top=0
            for z in range(max_h):

                out_html=out_html+'<div style="align-items: center;position: absolute;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;top:'+str(top)+'vh;left:'+str(left+(left*0.1))+'vh;"><span class="table_noselect" style="top:5px;align-items: center;height: '+str(circleh)+'vh; width: '+str(circleh)+'vh; border-radius: 50%; display: inline-block;position: relative"><form method="post" style="position: absolute;align-items: center;height:'+str(circleh)+ 'vh;'+' width:'+str(circleh)+'vh;"><button type="submit" name="table_home" value="1" style="background-color: blue;top:'+str((circleh/2)-(circleh/5))+ 'vh;color: white;border: none;border-radius: 70%;position: relative;padding:'+str(circleh/10)+'vh;font-size: 16px;"><input type="hidden" name="id_table" required="" id="id_table" value="'+str(i+1)+str(z+1)+'">'+str(i+1)+str(z+1)+'</button></form></span></div>'
                top=top+height
            left=left+widht
        

        return out_html