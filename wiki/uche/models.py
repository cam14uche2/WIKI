import email
from django.db import models



class User(models.Model):
    first_name = models.CharField('UserName', max_length= 200)
    last_name = models.CharField('UserName', max_length= 200)
    phone = models.CharField('contact phone', max_length= 17)
    email_address = models.EmailField('Email Address')
    



def __str__(self):
    return self.first_name + '' + self.last_name