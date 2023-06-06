from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def send_email(mail,pwd,usr):
    subject = 'Your generated login details'
    message = 'Your username is: '+ usr+ ' .Your initial password is: '+pwd+' I highly reccomend you change this password.'
    from_email = 'Matei Velich'

    send_mail(subject, message, from_email, [mail],fail_silently=True)
