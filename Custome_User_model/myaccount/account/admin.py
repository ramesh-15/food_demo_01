from django.contrib import admin
from .models import User,Users_donations,Contact
# Register your models here.
class session1(admin.ModelAdmin):
    list_display = ('id','food_name','food_type','quantity','donar_contact','food_pick_up','pincode','date','flag')

admin.site.register(User)
admin.site.register(Users_donations,session1)
admin.site.register(Contact)