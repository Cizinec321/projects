from pickle import FALSE
from django import forms
from .models import *
from django.contrib.auth import get_user_model

user=get_user_model()

class m_registerform(forms.Form):
    username=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 40px;font-size: 200%;","Placeholder":"Username"})
    )

    email=forms.EmailField(required=True,
    label='',
        widget=forms.Textarea(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 120px;font-size: 200%","Placeholder":"E-Mail"})
    )
    no_party=forms.EmailField(required=True,
    label='',
        widget=forms.NumberInput(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 120px;font-size: 200%","Placeholder":"Number of expected participants"})
    )

class registerform(forms.Form):

    username=forms.CharField(label='Utilizator')
    email=forms.EmailField(required=True, label='E-mail')
    participants=forms.CharField(widget=forms.NumberInput, required=True, label='Participanți')

class prefferences (forms.Form):



    def __init__(self, n,seat_no=None,r_name=None,email=None,menu_pref=None,f_comm=None,party=None,  *args, **kwargs):

        super(prefferences, self).__init__(*args, **kwargs)
        CHOICES_MENU =(
        ("Mănânc orice", "Mănânc orice"),
        ("Nu mănânc pește", "Nu mănânc pește"),
        ("Nu mănânc pește și carne", "Nu mănânc pește și carne"),
        ("Nu mănânc carne", "Nu mănânc carne"),
        ("Meniu copii", "Meniu copii"),
        ("Altele (menționați in comentarii)", "Altele (menționați in comentarii)"),
        )
        CHOICES_PARTY=(
            ("Da","Da"),
            ("Nu","Nu")
        )
        for i in range(1, n+1):
            self.fields["Seat_%d" % i] = forms.CharField(initial=seat_no[i-1],label='Locul %d' % i,widget=forms.Textarea(attrs={'style':"background: grey;width:70%;height:20px;"}))
            self.fields["Participant_Name_%d" % i] = forms.CharField(initial=r_name[i-1],label='Nume participant',required=True,widget=forms.Textarea(attrs={'style':"width:70%;height:20px;"}))
            self.fields["Participation_%d" % i] = forms.ChoiceField(initial=party[i-1],label='Confirmare participare',choices = CHOICES_PARTY,widget=forms.Select(attrs={'style':"width:72%;height:20px;"}))
            self.fields["Email_Adrress_%d" % i] = forms.CharField(initial=email[i-1],label='Adresă e-mail',required=False,widget=forms.Textarea(attrs={'style':"width:70%;height:20px;"}))
            self.fields["Menu_prefference_%d" % i] = forms.ChoiceField(initial=menu_pref[i-1],label='Preferințe culinare',choices = CHOICES_MENU,widget=forms.Select(attrs={'style':"width:72%;height:20px;"}))
            self.fields["Freeform_comments_%d" % i] = forms.CharField(initial=f_comm[i-1],label='Comentarii',required=False,widget=forms.Textarea(attrs={'style':"width:70%;height:20px;"}))



class m_prefferences (forms.Form):



    def __init__(self, n,seat_no=None,r_name=None,menu_pref=None,f_comm=None,party=None,  *args, **kwargs):

        super(m_prefferences, self).__init__(*args, **kwargs)
        CHOICES_MENU =(
        ("We will eat anything", "We will eat anything"),
        ("No fish", "No fish"),
        ("No meat, no fish", "No meat, no fish"),
        ("No meat", "No meat"),
        ("Children's menu", "Children's menu"),
        ("Other (specify in coments)", "Other (specify in coments)"),
        )
        CHOICES_PARTY=(
            ("Yes","Yes"),
            ("No","No")
        )
        for i in range(1, n+1):
            self.fields["Seat_%d" % i] = forms.CharField(initial=seat_no[i-1],widget=forms.Textarea(attrs={'style':"left:5px;position:relative;width:90%;height:30px;border: 20;background: grey;outline: 2;top: 0px;font-size: 60%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;"}))
            self.fields["Participant_Name_%d" % i] = forms.CharField(initial=r_name[i-1],required=True,widget=forms.Textarea(attrs={'style':"left:5px;position:relative;width:90%;height:30px;border: 20;background: white;outline: 2;top: 0px;font-size: 60%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;"}))
            self.fields["Participation_%d" % i] = forms.ChoiceField(initial=party[i-1],choices = CHOICES_PARTY,widget=forms.Select(attrs={'style':"left:5px;position:relative;width:90%;height:60px;border: 20;background: white;outline: 2;top: 0px;font-size: 60%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;"}))
            self.fields["Email_Adrress_%d" % i] = forms.CharField(initial=f_comm[i-1],required=False,widget=forms.Textarea(attrs={'style':"left:5px;position:relative;width:90%;height:30px;border: 20;background: white;outline: 2;top: 0px;font-size: 60%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;"}))
            self.fields["Menu_prefference_%d" % i] = forms.ChoiceField(initial=menu_pref[i-1],choices = CHOICES_MENU,widget=forms.Select(attrs={'style':"left:5px;position:relative;width:90%;height:60px;border: 20;background: white;outline: 2;top: 0px;font-size: 60%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;"}))
            self.fields["Freeform_comments_%d" % i] = forms.CharField(initial=f_comm[i-1],required=False,widget=forms.Textarea(attrs={'style':"left:5px;position:relative;width:90%;height:30px;border: 20;background: white;outline: 2;top: 0px;font-size: 60%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;"}))
            

class loginform(forms.Form):
    username=forms.CharField(label='Nume de utilizator')
    password=forms.CharField(
        widget=forms.PasswordInput,label='Parolă'
    )

class m_loginform(forms.Form):
    username=forms.CharField(label='',
        widget=forms.Textarea(attrs={'style':"right:15%;position:absolute;width:70%;height:60px;border: 2;background: white;outline: 2;top: 40px;font-size: 100%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;","Placeholder":"Username"})
    )
    password=forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'style':"right:15%;position:absolute;width:70%;height:60px;border: 2;background: white;outline: 2;top: 150px;font-size: 100%;text-align: center;font-family: Arial, Helvetica, sans-serif;padding-top: 10px;padding-bottom: 10px;","Placeholder":"Password"})
    )

class changepwd(forms.Form):
    password1=forms.CharField(
        widget=forms.PasswordInput
    )
    password2=forms.CharField(
        widget=forms.PasswordInput
    )
class m_changepwd(forms.Form):
    password1=forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'style':"right:15%;position:absolute;width:70%;height:60px;border: 2;background: white;outline: 0;top: 40px;font-size: 50%","Placeholder":"Type Password"})
    )
    password2=forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'style':"right:15%;position:absolute;width:70%;height:60px;border: 2;background: white;outline: 0;top: 120px;font-size: 50%","Placeholder":"Re-Type Password"})
    )

class input_form(forms.Form):
    #UN=forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols':50, 'style':"left:5%;position:relative;"}), disabled=True)
    HAP=forms.CharField(widget=forms.Textarea(attrs={'style':"left:5%;position:absolute;width:90%;height:50%;border: 2;background: white;outline: 0;bottom: 10vh"}))


class m_input_form(forms.Form):
    #UN=forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols':50, 'style':"left:5%;position:relative;"}), disabled=True)
    HAP=forms.CharField(widget=forms.Textarea(attrs={'style':"left:5%;position:absolute;width:90%;height:20%;border: 2;background: white;outline: 0;bottom: 30vh"}))


class seating_generator(forms.Form):
        vertical=forms.CharField(widget=forms.NumberInput, required=False)
        horizontal=forms.CharField(widget=forms.NumberInput, required=False, label='Orizontal')
        no_seats=forms.CharField(widget=forms.NumberInput, required=False, label='Nr locuri')
        name=forms.CharField(required=False, label='Nume')
        template= forms.ModelChoiceField(
        queryset=tables.objects.values_list("setting_name", flat=True).distinct(), required=False, label='Model'
    )

class m_seating_generator(forms.Form):
        vertical=forms.CharField(widget=forms.NumberInput(attrs={'style':"width:95%;height:100%;font-size: 50%;"}), required=False)
        horizontal=forms.CharField(widget=forms.NumberInput(attrs={'style':"width:95%;height:40%;font-size: 50%;"}), required=False)
        no_seats=forms.CharField(widget=forms.NumberInput(attrs={'style':"width:95%;height:40%;font-size: 50%;"}), required=False)
        name=forms.CharField(required=False)
        template= forms.ModelChoiceField(
        queryset=tables.objects.values_list("setting_name", flat=True).distinct(), required=False
    )


class invitees_form(forms.Form):

    name = forms.ModelChoiceField(invitees.objects.values_list("real_name", flat=True).filter(particpation='Da'), required=False, label='Nume participant')
    table_id=forms.CharField(disabled=False, label='ID Masă')
    setting_name=forms.CharField(disabled=True, label='Nume model')
    assigned_seats=forms.CharField(disabled=True,label='Locuri ocupate')
    already_seated=forms.CharField(widget=forms.Textarea,disabled=True, label='Persoane așezate')

class invitees_form_non_su(forms.Form):
    assigned_seats=forms.CharField(disabled=True, label='Locuri ocupate')
    already_seated=forms.CharField(widget=forms.Textarea,disabled=True, label='Persoane așezate')

class invitees_disp(forms.Form):

    table_id=forms.CharField(disabled=True)
    assigned_seats=forms.CharField(disabled=True)



class m_invitees_disp(forms.Form):

    table_id=forms.CharField( disabled=True)
    assigned_seats=forms.CharField( disabled=True)






    