from django import forms
from shelter.models import Caregiver


class CaregiverForm(forms.ModelForm):
    meno            = forms.CharField()
    priezvisko      = forms.CharField()
    datum_narodenia = forms.DateField()
    
    class Meta:
        model = Caregiver
        fields = [
            'meno',
            'priezvisko',
            'datum_narodenia'
        ]
