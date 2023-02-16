from django import forms
from .models import food_requests

class DonarDonateForm(forms.Form):
    food_name = forms.CharField(error_messages={'required':'Enter food name '})
    option = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = forms.ChoiceField(choices=option)
    quantity = forms.IntegerField()
    donar_contact = forms.CharField(max_length=10)
    food_pick_up = forms.CharField(max_length=200)
    pincode = forms.CharField(max_length=6)


# request food NGO
class FoodRequestForm(forms.ModelForm):
    class Meta:
        model = food_requests

        fields = ['food_id', 'food_name', 'username', 'pickup_point', 'donar_contact']