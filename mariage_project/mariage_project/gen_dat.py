from .models import in_form, tables, models, invitees,invitees_x_table
from .forms import prefferences
from django.contrib.auth import get_user_model
import random
import string

def gen_text(lng):
        if lng=='EN':
            outval='<div class="main_hidetxt" id="aboutus">'\
                    '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em;background: rgba(255, 255, 255, 0.7); margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>About us</b><br><br>'\
                    'We are Bianca and Matei - or Bia and Matei, Bianca and Edi, Bianca and Eduard. Before we were Bianca and Matei, we were Bianca, HR Team UK advusor and Matei, the guy with the reports, SAP and automatization from BAS. We worked for the same company, same function, sometimes the same floor, but we were far from being in love. On the contrary, Bianca had a deep antipathy mixed with fear for Matei. Around summer 2018, Matei thought that Bianca is a cool gal and, according to him, started flirting. But his efforts were not noticed, because Bianca was busy regulating her blood pressure after every e-mail with grammar mistakes she got from Matei.<br><br>'\
                    'During winter 2018, we started working toghether on a project. Spending allot of time toghether and often the alst desperate people on the 4th floor still working at 7PM, Bianca''s anthypathy and fear transformed into sympathy. When Matei mentioned one of his reccuring nightmare and Bianca noticed it''s the same one as hers, specifically taking a math test, Bianca knew they were supposed to, at least, be friends. After some more weeks, Bianca jokingly told a friend that she will marry Matei if he fixed a tool for her, which he did, thus sealing their fate.<br><br>'\
                    'On December 16th 2018, Bianca texted “LMA și SCM” (Happy birthday) to Matei , and extended their discussions from Skype for Business and Outlook to texting outside working hours. So, the flirting started from both sides, salted with jokes stolen from Sector 7, which worked so well (thanks to our advanced flirting skills), that in February 2019 was still exclusivelly professional, but with allot of laughter thanks to our joke exchanges.<br><br>'\
                    'On 22nd February, Bianca took heart and told Matei she bought him a house warming gift, and Matei took hearth and askedd Bianca out for dinner. We went on our first date on 23rd February, had a good time and knew we would spend the rest of our time toghether. Of course we didn''t tell each other that, so it took one more month untill we told each other we want a relationship.<br><br>'\
                    'Am început de atunci sa ne clădim viața de cuplu, sa iubim fiecare minut din proces, și sa ne iubim unul pe celălalt.<br><br>'\
                    'We were toghether trough dreams-come-true, job changes, a pandemic, unique experiences, apartment renovations, health challenges, we discovered each other, we overcame obstacles, travelled, ate, laughed, got beaten by Ellie(our pet cat), got cat kisses Ellie(our pet cat), we filled our lives with love and peace. If there is one thing we are certain about, it''s that we want to spend the rest of our live toghether, so we want to become a family in front of God and the law, on 1st of June 2024.<br><br>'\
                    'Because you are a part of our life, we would like you to celebrate with us while we write the next chapters of our lives.<br>'\
                    '</div>'\
                    '<div class="main_hidetxt" id="aboutyou">'\
                    '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em;background: rgba(255, 255, 255, 0.7); margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>About you and your participation</b><br><br>'\
                    "Because we are a organised and tech savy couple, we would appreciate if you could use the form on this website to RSVP, fill in your dietary prefferences and contact details.<br><br>"\
                    "We will start with the legal ceremony at Village by the Lake in Gilău, saturday 1st of June 2024 11:00AM, and the religious ceremony will take place at the All Saints catholic church in Florești 02:00PM.<br><br>"\
                    "The party will be at Wonderland, Orhideea lounge, starting with 03:30PM.<br><br>"\
                    "Most probably you got a link or a QR code. If you access that link or scan the QR code, you should be loged in with your unique account name and password. If this didn't happen, pelase contact us.<br><br>"\
                    "In the Seating Plan section, once one was finalised and published, you will find the seating plan. The table you were assigned to will have it's number in a red circle. If a seating plan hasn't been published, you will receive a warning message. If this is the case, please be patient and check again later.<br><br>"\
                    "In the participant admin section, ou will find the details of your unique account. Here you can confirm the aprticipation of each family member. Also, here you will find a list of participants from your family and will be able to edit their names, dietary restrictions and prefferences, contact details and a comment section. Please use them, we will read all of them."\
                    "</p>"\
                    '</div>'\
                    '<div class="main_hidetxt" id="contact">'\
                    '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 5em; margin-bottom: 0em; text-align: left;"><b>Contact</b><br><br><br>'\
                    "<b>Email:</b> velich.eduard[at]gmail.com<br>"\
                    '</div>'
             
        else:
            outval='<div class="main_hidetxt" id="aboutus">'\
                    '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em;background: rgba(255, 255, 255, 0.7); margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>Despre noi</b><br><br>'\
                    'Suntem Bianca și Matei - sau Bia și Matei, Bianca și Edi, Bianca și Eduard. Înainte sa fim Bianca si Matei, eram Bianca, advisorul din HR Team UK si Matei, tipul cu rapoarte, SAP și automatizări din BAS. Lucram la aceeași companie, in aceeași funcțiune, uneori la același etaj, dar eram departe de a fi îndrăgostiți unul de altul. Din contra, Bianca nutrea o profunda antipatie amestecată cu frica fata de Matei. Prin vara anului 2018, lui Matei i s-a părut ca Bianca e o tipa mișto și, susține el, a început sa flirteze cu ea, dar eforturile i-au trecut complet neobservate, caci Bianca era ocupată sa își regleze tensiunea la fiecare mail cu erori găsite in sistem primite de la Matei.<br><br>'\
                    'Pe la începutul iernii 2018, am început sa lucram împreuna la un proiect de automatizare. Petrecând destul de mult împreuna și adesea rămânând ultimii disperați de la etajul 4 încă lucrând la ora 19, antipatia și frica Biancăi s-au transformat in simpatie. Când Matei i-a spus Biancăi ca unul dintre coșmarurile lui recurente este identic cu al ei, anume test/teza la mate, Bianca a știut ca trebuie sa fie unul parte din viața ceiluilalt, măcar ca buni prieteni. După alte câteva săptămâni, de altfel, Bianca i-a spus prietenei ei ca dacă Matei ii repara ceva la instrumentul de automatizare, se și mărita cu el - Matei a reparat, deci practic soarta a fost pecetluită din acel moment.<br><br>'\
                    'Pe 16 Decembrie 2018, Bianca i-a scris “LMA și SCM” lui Matei pe messenger, și a extins altfel discuțiile noastre de pe Skype for Business și Outlook la messenger in afara orelor de munca. A început de atunci un flirt din ambele părți, presărat cu glume furate de la Sector 7, care a mers așa de bine (datorită capacității noastre avansate de a flirta), încât in Februarie 2019 relația noastră era in continuare exclusiv profesională, cu multe râsete datorate mesajelor virtuale.<br><br>'\
                    'Pe 22 Februarie, Bianca și-a luat inima in dinți și i-a spus lui Matei ca i-a luat un cadou de casa noua, iar Matei și-a luat și mai mult inima in dinți și a invitat-o pe Bianca la o cina. Am ieșit pentru prima data pe 23 Februarie, ne-am simțit foarte bine, și am știut ca vrem sa ne petrecem restul timpului unul cu celălalt. Desigur ca nu ne-am spus asta, așa ca a mai durat aproape o luna pana ne-am decis sa facem pasul important de a avea o relație.<br><br>'\
                    'Am început de atunci sa ne clădim viața de cuplu, sa iubim fiecare minut din proces, și sa ne iubim unul pe celălalt.<br><br>'\
                    'Am fost impreuna prin vise împlinite, schimbări de job, pandemie, experiențe unice, finisaje de apartamente, provocări de sănătate fizica și psihică, ne-am descoperit unul pe altul si pe noi înșine, ne-am depășit bariere, am călătorit, am mancat, am ras, ne-am luat bătaie de la Ellie, am luat pupici de la Ellie, ne-am umplut viața de iubire și liniște interioară. Dacă e un lucru de care suntem siguri, e ca vrem sa continuam asta pentru tot restul vieții noastre, așa ca ne dorim sa devenim o familie si in fata legii si a lui Dumnezeu, in data de 1 Iunie 2024.<br><br>'\
                    'Pentru ca sunteți parte din viața noastră, ne dorim sa ne fiti alături in aceasta data, cât si in timp ce scriem noile capitole ale vieții noastre.<br>'\
                    '</div>'\
                    '<div class="main_hidetxt" id="aboutyou">'\
                    '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em;background: rgba(255, 255, 255, 0.7); margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>Despre voi și participarea voastră</b><br><br>'\
                    "Pentru că suntem un cuplu ultra conectat la tehnologie si organizat, vă rugăm să folosiți formularul pentru a ne confirma prezența voastră la nuntă, cât si detalii legate despre preferințe alimentare, si mai ales date de contact.<br><br>"\
                    "Vom incepe cu o ceremonie la Village by The Lake in comuna Gilău, sămbătă 1 Iunie 2024 ora 11:00, iar Cununia Religioasă va avea loc la Biserica Catolică Toți Sfinții din Florești ora 14:00.<br><br>"\
                    "Petrecerea va avea loc la Wonderland, sala Orhideea, incepând cu ora 15:30.<br><br>"\
                    "Cel mai probabil că ați primit un link sau un cod QR. Dacă accesați acel link sau scanați codul, ar trebui sa fiți conectați cu un cont dedicat cu nume de utilizator si parolă unice. În cazul in care acest lucru nu s-a întâmplat, vă rog sa ne contactați.<br><br>"\
                    "În secțiunea Plan de așezare, odată ce va fi finalizat, veți găsi mesele. Masa la care ați fost așezat, va avea numărul colorat cu roșu. Dacă un plan de așezare nu a fost publicat, veți intampina un mesaj de avertizare. În cazul acesta, vă rugăm sa verificați pagina mai tărziu.<br><br>"\
                    "În secțiunea Administrare participanți, veți găsi detaliile contului dumneavoastră unic. Aici puteți confirma participarea fiecărui membru din familie in parte. De asemenea, aici veți găsi numărul de participanți din partea familiei dumneavoastră și veți avea posibilitatea să editați numele acestora, restricțiile alimentare, detaliile de contact cât și o secțiune de comentarii. Vă rugam sa le folosiți. Le vom citit pe toate."\
                    "</p>"\
                    '</div>'\
                    '<div class="main_hidetxt" id="contact">'\
                    '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 5em; margin-bottom: 0em; text-align: left;"><b>Contact</b><br><br><br>'\
                    "<b>Email:</b> velich.eduard[at]gmail.com<br>"\
                    '</div>'
        return outval



def get_party_full():
    User = get_user_model()
    users = User.objects.all()
    outval='<table style="top: 5%;position: relative; table-layout: fixed ; width: 100%; "><tbody>'
    but_count=0
    for x in  users:
        if str(x.username)!='admin':
            query_res=invitees.objects.filter(name__startswith=str(x.username)).count()  
            party_res=invitees.objects.filter(name__startswith=str(x.username),particpation='Da').count()    
            outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.username)+'</label></th>'+'<th style="text-align: left;"><label >'+str(query_res)+' Locuri</label></th>'+'<th style="text-align: left;"><label >'+str(party_res)+' Participanți</label></th>'+'<th style="text-align: left;"><form method="post"><button type="submit" name="delete_participant" value="'+str(x.username)+'" class="pos_button2">Șterge</button></form></th>'+'<th style="text-align: left;"><form method="post"><button type="button" name="edit_participant" value="'+str(x.username)+'" class="pos_button2" onclick=document.getElementById('+chr(39)+str(but_count)+'utiz'+chr(39)+').className='+chr(39)+'dropbtn2_show'+chr(39)+'>Detalii</button></form></th></tr>'
            but_count=but_count+1
    outval=outval+'</tbody></table>'
    return outval

def get_party_full_non_su(unm, lang):

    outval='<table style="top: 5%;position: relative; table-layout: fixed ; width: 100%; "><tbody>'
    but_count=0

    if str(unm)!='admin':
            query_res=invitees.objects.filter(name__startswith=str(unm)).count()  
            party_res=invitees.objects.filter(name__startswith=str(unm),particpation='Da').count()   
            if lang=='EN':
                outval=outval+'<tr><th style="text-align: left;"><label >'+str(unm)+'</label></th>'+'<th style="text-align: left;"><label >'+str(query_res)+' Seats</label></th>'+'<th style="text-align: left;"><label >'+str(party_res)+' Participants</label></th>'+'<th style="text-align: left;"></th>'+'<th style="text-align: left;"><form method="post"><button type="button" name="edit_participant" value="'+str(unm)+'" class="pos_button2" onclick=document.getElementById('+chr(39)+str(but_count)+'utiz'+chr(39)+').className='+chr(39)+'dropbtn2_show'+chr(39)+'>Details</button></form></th></tr>'
            else: 
                outval=outval+'<tr><th style="text-align: left;"><label >'+str(unm)+'</label></th>'+'<th style="text-align: left;"><label >'+str(query_res)+' Locuri</label></th>'+'<th style="text-align: left;"><label >'+str(party_res)+' Participanți</label></th>'+'<th style="text-align: left;"></th>'+'<th style="text-align: left;"><form method="post"><button type="button" name="edit_participant" value="'+str(unm)+'" class="pos_button2" onclick=document.getElementById('+chr(39)+str(but_count)+'utiz'+chr(39)+').className='+chr(39)+'dropbtn2_show'+chr(39)+'>Detalii</button></form></th></tr>'
            but_count=but_count+1
    outval=outval+'</tbody></table>'
    return outval




def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def details_load():

    User = get_user_model()
    users = User.objects.all()
    form_list=[]

    
    
    for items in users:
        if str(items.get_username())!='admin':
            query_res=invitees.objects.filter(name__startswith=str(items.get_username())+' - seat').count()
            seats_list=[]
            real_name=[]
            mail=[]
            menu_pref=[]
            f_comm=[]
            party=[]
            for x in invitees.objects.filter(name__startswith=str(items.get_username())+' - seat').all():
                seats_list.append(str(x.name))
                real_name.append(str(x.real_name))
                mail.append(str(x.e_mail))
                menu_pref.append(str(x.menu_prefference))
                f_comm.append(str(x.Freeform_comments))
                party.append(str(x.particpation))
            prefferences_inst = prefferences(query_res,seat_no=seats_list,r_name=real_name,email=mail,menu_pref=menu_pref,f_comm=f_comm,party=party)
            form_list.append(prefferences_inst)
    return form_list

def details_load_non_su(unm, lng):

    form_list=[]
    if str(unm)!='admin':
            query_res=invitees.objects.filter(name__startswith=str(unm)+' - seat').count()
            seats_list=[]
            real_name=[]
            menu_pref=[]
            f_comm=[]
            party=[]
            mail=[]
            for x in invitees.objects.filter(name__startswith=str(unm)+' - seat').all():
                seats_list.append(str(x.name))
                real_name.append(str(x.real_name))
                menu_pref.append(str(x.menu_prefference))
                f_comm.append(str(x.Freeform_comments))
                party.append(str(x.particpation))
                mail.append(str(x.e_mail))
            prefferences_inst = prefferences(query_res,seat_no=seats_list,r_name=real_name,email=mail,menu_pref=menu_pref,f_comm=f_comm,party=party,lng=lng)
            form_list.append(prefferences_inst)
    return form_list