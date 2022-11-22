from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class VetForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]

# class CaregiverForm(forms.ModelForm):
#     meno            = forms.CharField()
#     priezvisko      = forms.CharField()
#     datum_narodenia = forms.DateField()
    
#     class Meta:
#         model = Caregiver
#         fields = [
#             'meno',
#             'priezvisko',
#             'datum_narodenia'
#         ]
