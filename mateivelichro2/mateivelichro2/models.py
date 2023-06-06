from django.db import models
from django.contrib.auth.models import User, Group






class contact(models.Model):

    managed=True
    db_table = "'contact'"
    Full_Name=models.CharField(max_length=250)
    Company=models.CharField(max_length=250)
    Position=models.CharField(max_length=250)
    EMAIL=models.CharField(max_length=250)
    Phone=models.CharField(max_length=250)
    Message=models.CharField(max_length=250)
    
