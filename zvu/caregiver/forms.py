from django import forms
from .models import Caregiver


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


# class RawCaregiverForm(forms.Form):
#     title       = forms.CharField()
#     description = forms.CharField(
#                         required=False, 
#                         widget=forms.Textarea(
#                                 attrs={
#                                     "placeholder": "Your description",
#                                     "class": "new-class-name two",
#                                     "id": "my-id-for-textarea",
#                                     "rows": 20,
#                                     'cols': 120
#                                 }
#                             )
#                         )
#     price       = forms.DecimalField(initial=199.99)