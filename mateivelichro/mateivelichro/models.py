from django.db import models

class in_form(models.Model):
    UN_DB=models.CharField(max_length=200)
    HAP_DB=models.CharField(max_length=200)

