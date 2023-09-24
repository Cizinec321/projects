from .models import in_form, tables, models, invitees,invitees_x_table
from .forms import prefferences
from django.contrib.auth import get_user_model
import random
import string

def gen_text():
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

def get_party_list(table_id,setting_id):

    query_res=invitees_x_table.objects.filter(table_id=table_id,setting_name=setting_id)
    outval='<table style="top: 5%;position: relative;"><tbody><tr><th style="text-align: left;"><label >Seated invitees:<br><br></label></th></tr>'
    for x in  query_res:
        outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.r_name)+'</label></th></tr>'
    outval=outval+'</tbody></table>'
    return outval
def get_party_names(table_id,setting_id):

    query_res=invitees_x_table.objects.filter(table_id=table_id,setting_name=setting_id)
    outval='<table style="top: 5%;position: relative;"><tbody><tr><th style="text-align: left;"><label >Seated invitees:<br><br></label></th></tr>'
    for x in  query_res:
        outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.name)+'</label></th></tr>'
    outval=outval+'</tbody></table>'
    return outval

def get_party_full():
    User = get_user_model()
    users = User.objects.all()
    outval='<table style="top: 5%;position: relative; table-layout: fixed ; width: 100%; "><tbody>'
    but_count=0
    for x in  users:
        if str(x.username)!='admin':
            query_res=invitees.objects.filter(name__startswith=str(x.username)).count()  
            party_res=invitees.objects.filter(name__startswith=str(x.username),particpation='Yes').count()    
            outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.username)+'</label></th>'+'<th style="text-align: left;"><label >'+str(query_res)+' Seats</label></th>'+'<th style="text-align: left;"><label >'+str(party_res)+' Participants</label></th>'+'<th style="text-align: left;"><form method="post"><button type="submit" name="delete_participant" value="'+str(x.username)+'" class="pos_button2">Delete</button></form></th>'+'<th style="text-align: left;"><form method="post"><button type="button" name="edit_participant" value="'+str(x.username)+'" class="pos_button2" onclick=document.getElementById('+chr(39)+str(but_count)+'utiz'+chr(39)+').className='+chr(39)+'dropbtn2_show'+chr(39)+'>Details</button></form></th></tr>'
            but_count=but_count+1
    outval=outval+'</tbody></table>'
    return outval

def get_party_full_non_su(unm):

    outval='<table style="top: 5%;position: relative; table-layout: fixed ; width: 100%; "><tbody>'
    but_count=0

    if str(unm)!='admin':
            query_res=invitees.objects.filter(name__startswith=str(unm)).count()  
            party_res=invitees.objects.filter(name__startswith=str(unm),particpation='Yes').count()    
            outval=outval+'<tr><th style="text-align: left;"><label >'+str(unm)+'</label></th>'+'<th style="text-align: left;"><label >'+str(query_res)+' Seats</label></th>'+'<th style="text-align: left;"><label >'+str(party_res)+' Participants</label></th>'+'<th style="text-align: left;"></th>'+'<th style="text-align: left;"><form method="post"><button type="button" name="edit_participant" value="'+str(unm)+'" class="pos_button2" onclick=document.getElementById('+chr(39)+str(but_count)+'utiz'+chr(39)+').className='+chr(39)+'dropbtn2_show'+chr(39)+'>Details</button></form></th></tr>'
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

def details_load_non_su(unm):

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
            prefferences_inst = prefferences(query_res,seat_no=seats_list,r_name=real_name,email=mail,menu_pref=menu_pref,f_comm=f_comm,party=party)
            form_list.append(prefferences_inst)
    return form_list