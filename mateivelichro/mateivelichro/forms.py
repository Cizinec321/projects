from django import forms
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

class registerform(forms.Form):
    username=forms.CharField()

    email=forms.EmailField(required=True)


class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(
        widget=forms.PasswordInput
    )

class m_loginform(forms.Form):
    username=forms.CharField(label='',
        widget=forms.Textarea(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 40px;font-size: 200%;","Placeholder":"Username"})
    )
    password=forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 120px;font-size: 200%","Placeholder":"Password"})
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
        widget=forms.PasswordInput(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 40px;font-size: 200%","Placeholder":"Type Password"})
    )
    password2=forms.CharField(label='',
        widget=forms.PasswordInput(attrs={'style':"right:15%;position:absolute;width:70%;height:40px;border: 2;background: white;outline: 0;top: 120px;font-size: 200%","Placeholder":"Re-Type Password"})
    )

class input_form(forms.Form):
    #UN=forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols':50, 'style':"left:5%;position:relative;"}), disabled=True)
    HAP=forms.CharField(widget=forms.Textarea(attrs={'style':"left:5%;position:absolute;width:90%;height:50%;border: 2;background: white;outline: 0;bottom: 10vh"}))


class m_input_form(forms.Form):
    #UN=forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols':50, 'style':"left:5%;position:relative;"}), disabled=True)
    HAP=forms.CharField(widget=forms.Textarea(attrs={'style':"left:5%;position:absolute;width:90%;height:20%;border: 2;background: white;outline: 0;bottom: 30vh"}))


