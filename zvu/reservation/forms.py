from django import forms
from shelter.models import Reservation, Animal, Volunteer
from django.contrib.auth.models import User

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.meno

class ReservationForm(forms.ModelForm):
    datum_vytvorenia = forms.DateField()
    rezervovany_od = forms.DateField()
    rezervovany_od = forms.DateField()
    zvieraid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Zviera'
    )
               
    class Meta:
        model = Reservation
        fields = [
            'datum_vytvorenia',
            'rezervovany_od',
            'rezervovany_do',
            'zvieraid'
        ]
    
    
class ReservationManageForm(forms.ModelForm):
    datum_vytvorenia = forms.DateField()
    rezervovany_od = forms.DateField()
    rezervovany_od = forms.DateField()
    # schvalenie = forms.ChoiceField(choices=[(0,'neschválená'),(1,'schválená')],required=False)
    schvalenie = forms.IntegerField()
    stav = forms.ChoiceField(choices=[('čakajúca','čakajúca'),
                                      ('prebihajúca','prebihajúca'),
                                      ('dokončená','dokončená')],
                             required=False)
    zvieraid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Zviera'
    )
    dobrovolnikid = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='volunteer')
        # label='User'
    )
               
    class Meta:
        model = Reservation
        fields = [
            'datum_vytvorenia',
            'rezervovany_od',
            'rezervovany_do',
            'schvalenie',
            'stav',
            'zvieraid',
            'dobrovolnikid'
        ]

