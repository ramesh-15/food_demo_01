from django import forms
from .models import Doner_details

class Donar_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Doner_details
        fields ='__all__'
    def cleaned_dd_username(self):
        cleaned_data = super().clean()
        name = cleaned_data['dd_username']
        if len(name)<5:
            raise forms.ValidationError('user name should be atleast 5 character!!!')
        return name
