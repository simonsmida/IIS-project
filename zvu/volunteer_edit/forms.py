from django import forms
from shelter.models import Volunteer


class VolunteerForm(forms.ModelForm):
    meno            = forms.CharField()
    priezvisko      = forms.CharField()
    datum_narodenia = forms.DateField()
    doveryhodnost = forms.ChoiceField(choices=[('0','neschválený'),('1','schválený')],required=False)
    
    class Meta:
        model = Volunteer
        fields = [
            'meno',
            'priezvisko',
            'datum_narodenia',
            'doveryhodnost'
        ]
