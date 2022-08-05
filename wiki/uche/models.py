import email
from django.db import models




class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)



class User(models.Model):
    first_name = models.CharField('firstName', max_length= 200)
    last_name = models.CharField('LastName', max_length= 200)
    phone = models.CharField('contact phone', max_length= 17)
    email_address = models.EmailField('Email Address')



    



def __str__(self):
    return self.first_name + '' + self.last_name


