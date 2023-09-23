from django.shortcuts import render
from . import forms
from django.core.mail import send_mail
import base64
from io import StringIO
from . import texts
import requests
import json

def home(request):
    agent = request.META["HTTP_USER_AGENT"]
    mobile=False
    comm_content_class='comm-content'
    if 'Mobile' in agent: 
          mobile=True
          comm_content_class='m_comm-content'

    pers_dat_form=forms.contact(request.POST or None)  


    
    steam_plate=gen_steam_plate()
    github_plate=gen_github_plate()

    if request.method=='POST':
                    if request.POST.get("register_form"):
                        print(pers_dat_form.errors)
                        if pers_dat_form.is_valid():
                            mail_body=''
                            for field in pers_dat_form.fields:
                                    
                                    mail_body=mail_body+str(field)+' : '+str(pers_dat_form.cleaned_data[field])+'''\r\n'''
                            send_mail(
                                        'Message via website',
                                        mail_body,
                                        "velich.eduard@gmail.com",
                                        ["velich.eduard@gmail.com"],
                                        fail_silently=False,
                                        )


                            return render(request,'landing_alt.html',{'display_trigger_comm':'<div id="comm_div" class="'+comm_content_class+'" style="display:block">','comm_msg':'Thank you! Your message was sent to my inbox. I will reply as soon as possible.','pers_data_form':pers_dat_form,'steam_plate':steam_plate,'github_plate':github_plate,'mobile':mobile})
                             
                        else:
                           return render(request,'landing_alt.html',{'display_trigger_comm':'<div id="comm_div" class="'+comm_content_class+'" style="display:block">','comm_msg':'Something went wrong. Please check the form and try again.','pers_data_form':pers_dat_form,'steam_plate':steam_plate,'github_plate':github_plate,'mobile':mobile})

    return render(request,'landing_alt.html',{'display_trigger_comm':'<div id="comm_div" class="'+comm_content_class+'" style="display:none">','pers_data_form':pers_dat_form,'steam_plate':steam_plate,'github_plate':github_plate,'mobile':mobile})



def gen_steam_plate():
    try:
        steamuser=requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=#####&steamids=76561198135210324').json()
        steamgame=requests.get('https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=#####&steamid=76561198135210324&format=json').json()
        img_src=steamuser['response']['players'][0]['avatarfull']
        steam_txt='<p class="p1l">Steam Handle: <a href="'+steamuser['response']['players'][0]['profileurl']+'">'+steamuser['response']['players'][0]['personaname']+'</a></p><p class="p1l"> Last played: '+steamgame['response']['games'][0]['name']+'</p><p class="p1s">Totaling '+str(steamgame['response']['games'][0]['playtime_2weeks'])+' minutes in the last 2 weeks.</p>'

        out_html='<div class="steam_wrapper"><div class="steam_pic" style="background-image: url('+img_src+');"></div><div class="steam_desc">'+steam_txt
        out_html=out_html+'</div></div>'
    except:
          out_html=''

    return out_html


def gen_github_plate():
    try:    
        githubuser=requests.get('https://api.github.com/users/cizinec321', headers={'Authorization': 'access_token #####'}).json() 
        githupublicrepos=requests.get('https://api.github.com/users/Cizinec321/repos', headers={'Authorization': 'access_token ######'}).json()
        
        img_src=githubuser['avatar_url']
        steam_txt='<p class="p1l">GitHub Handle: <a href="'+githubuser['html_url']+'">'+githubuser['login']+'</a></p><p class="p1l"> Public Repo: '+'<a href="'+githupublicrepos[0]['html_url']+'">'+githupublicrepos[0]['name']+'</a></p><p class="p1s">Last push: '+str(githupublicrepos[0]['pushed_at'])[0:10]+'</p>'

        out_html='<div class="steam_wrapper"><div class="steam_pic" style="background-image: url('+img_src+');"></div><div class="steam_desc">'+steam_txt
        out_html=out_html+'</div></div>'
    except:
          out_html=''

    return out_html