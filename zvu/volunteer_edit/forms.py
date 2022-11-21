from django import forms
from shelter.models import Volunteer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class VolunteerCreateForm(UserCreationForm):
    # meno            = forms.CharField()
    # priezvisko      = forms.CharField()
    # datum_narodenia = forms.DateField()
    trust = forms.ChoiceField(choices=[('0','neschválený'),('1','schválený')],required=False)
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]
        
class VolunteerChangeForm(UserChangeForm):
    # meno            = forms.CharField()
    # priezvisko      = forms.CharField()
    # datum_narodenia = forms.DateField()
    trust = forms.ChoiceField(choices=[('0','neschválený'),('1','schválený')],required=False)
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
