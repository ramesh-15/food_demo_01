from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, date


# Create your models here.

class User(AbstractUser):
    is_Donar = models.BooleanField('Donar')
    is_NGO = models.BooleanField('NGO')
    # dd_username = models.CharField(max_length=100, verbose_name='User Name', null=True, blank=True,default='')
    #
    # dd_email = models.EmailField(max_length=100, verbose_name='Email',default='')
    # phone_number = models.IntegerField(null=True,default='')
    # possibilites = (
    # ('1', 'Restaurent'), ('2', 'Mess'), ('3', 'Hotel'), ('4', 'Hostel'), ('5', 'Events'), ('6', 'Donation'),
    # ('7', 'Other'))
    # donation_from = models.CharField(default=True,max_length=100, choices=possibilites)
    # address = models.CharField(max_length=100, null=True, blank=True,default='')
    # pincode = models.CharField(max_length=10, null=True,default='')
    # city = models.CharField(max_length=100,default='')
    # state = models.CharField(max_length=100,default='')


# class Doner_details(models.Model):
#     dd_username=models.CharField(max_length=100,verbose_name='User Name',null=True,blank=True)
#     dd_email=models.EmailField(max_length=100,verbose_name='Email')
#     phone_number= models.IntegerField()
#     possibilites = (('1', 'Restaurent'),('2', 'Mess'), ('3', 'Hotel'), ('4', 'Hostel'),('5', 'Events'), ('6', 'Donation'), ('7', 'Other'))
#     donation_from = models.CharField(max_length=100 ,choices = possibilites)
#     address=models.CharField(max_length=100,null=True, blank=True)
#     pincode = models.CharField(max_length=10,null=True)
#     city=models.CharField(max_length=100)
#     state=models.CharField(max_length=100)
#     password = models.CharField(max_length=25,null=True)

# class NGO_Register(models.Model) :
#     org_name = models.CharField(max_length=100, verbose_name='Organiser Name')
#     register_id = models.CharField(max_length=50)
#     email      = models.EmailField()
#     address = models.CharField(max_length=100)
#     city    =models.CharField(max_length=100)
#     pincode = models.CharField(max_length=6)
#     contact = models.IntegerField()
#     pwd = models.CharField(max_length=50,verbose_name='password')
#     con_pwd = models.CharField(max_length=50,verbose_name=' confirm password')

class Users_donations(models.Model):

    food_name = models.CharField(max_length=100, verbose_name='Food Name')
    possibilities = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = models.CharField(max_length=100, choices=possibilities)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    donar_contact = models.CharField(max_length=10)
    food_pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    username = models.CharField(max_length=156,default=False)
    flag = models.CharField(max_length=12, default=False)

    def __str__(self):
        return (self.food_name)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


# class food_requests(models.Model):
#     food_id = models.ForeignKey(Users_donations, on_delete=models.CASCADE)
#     username = models.CharField(max_length=100)
#     food_name = models.CharField(max_length=100)
#     pickup_point = models.CharField(max_length=100)
#     donar_contact = models.CharField(max_length=100)
#     date = models.DateField(default=date.today())
#
#     def __str__(self):
#         return self.username