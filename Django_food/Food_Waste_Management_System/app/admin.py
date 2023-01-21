from django.contrib import admin
from .models import Doner_details
# Register your models here.

class session(admin.ModelAdmin):
    list_display = ('dd_username','dd_email','phone_number','donation_from','address','pincode','city','state')

admin.site.register(Doner_details,session)
