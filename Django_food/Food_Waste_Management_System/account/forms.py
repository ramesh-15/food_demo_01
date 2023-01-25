from django import forms
from .models import Doner_details
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register(UserCreationForm):


    # option = (('M',"Male"),("F","Female"))
    # gender = forms.ChoiceField(widget=forms.RadioSelect(),choices=option)
    class Meta:
        model = User
        #fields =['is_Donar','is_NGO','dd_username','dd_email','phone_number','donation_from','address','pincode','city','state']
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_Donar', 'is_NGO']


class donarloginform(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


