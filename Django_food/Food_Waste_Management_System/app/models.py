from django.db import models

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

