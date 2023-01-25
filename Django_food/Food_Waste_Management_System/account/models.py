from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Doner_details(models.Model):
    dd_username=models.CharField(max_length=100,verbose_name='User Name',null=True,blank=True)
    dd_email=models.EmailField(max_length=100,verbose_name='Email')
    phone_number= models.IntegerField()
    possibilites = (('1', 'Restaurent'),('2', 'Mess'), ('3', 'Hotel'), ('4', 'Hostel'),('5', 'Events'), ('6', 'Donation'), ('7', 'Other'))
    donation_from = models.CharField(max_length=100 ,choices = possibilites)
    address=models.CharField(max_length=100,null=True, blank=True)
    pincode = models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    password = models.CharField(max_length=25,null=True)

class NGO_Register(models.Model) :
    org_name = models.CharField(max_length=100, verbose_name='Organiser Name')
    register_id = models.CharField(max_length=50)
    email      = models.EmailField()
    address = models.CharField()
    city    =models.CharField()
    pincode = models.PositiveIntegerField()
    contact = models.IntegerField()
    pwd = models.CharField(max_length=50,verbose_name='password')
    con_pwd = models.CharField(max_length=50,verbose_name=' confirm password')

class User(AbstractUser):
    is_Donar = models.BooleanField('Donar')
    is_NGO = models.BooleanField('NGO')

