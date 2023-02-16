from django.contrib import admin
from .models import food_requests,Users_donations

# Register your models here.
class session1(admin.ModelAdmin):
    list_display = ('id','food_name','food_type','quantity','donar_contact','food_pick_up','pincode','flag','date')

class session2(admin.ModelAdmin):
    list_display = ('food_id','food_name','username','donar_contact','pickup_point','date','flag')


admin.site.register(Users_donations,session1)

admin.site.register(food_requests,session2)
