from django import forms
from shelter.models import Reservation, Animal
from django.contrib.auth.models import User

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ReservationForm(forms.ModelForm):
    creation_date = forms.DateField()
    reserved_from = forms.DateField()
    reserved_to = forms.DateField()
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal',
        widget=forms.HiddenInput()
    )
               
    class Meta:
        model = Reservation
        fields = [
            'creation_date',
            'reserved_from',
            'reserved_to',
            'animalid'
        ]
        
class ReservationUpdateForm(forms.ModelForm):
    creation_date = forms.DateField()
    reserved_from = forms.DateField()
    reserved_to = forms.DateField()
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal',
    )
               
    class Meta:
        model = Reservation
        fields = [
            'creation_date',
            'reserved_from',
            'reserved_to',
            'animalid'
        ]
            
    
class ReservationManageForm(forms.ModelForm):
    creation_date = forms.DateField()
    reserved_from = forms.DateField()
    reserved_to = forms.DateField()
    # approval = forms.ChoiceField(choices=[(0,'neschválená'),(1,'schválená')],required=False)
    approval = forms.IntegerField()
    state = forms.ChoiceField(choices=[('čakajúca','čakajúca'),
                                      ('prebihajúca','prebihajúca'),
                                      ('dokončená','dokončená')],
                             required=False)
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal'
    )
    volunteerid = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='volunteer'),
        label='Volunteer'
    )
               
    class Meta:
        model = Reservation
        fields = [
            'creation_date',
            'reserved_from',
            'reserved_to',
            'approval',
            'state',
            'animalid',
            'volunteerid'
        ]
