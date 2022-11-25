from django import forms
from shelter.models import Reservation, Animal
from django.contrib.auth.models import User

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class ReservationForm(forms.ModelForm):
    reserved_date = forms.DateField()
    reserved_from = forms.TimeField()
    reserved_to = forms.TimeField()
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal',
        widget=forms.HiddenInput()
    )
                         
    class Meta:
        model = Reservation
        fields = [
            'reserved_date',
            'reserved_from',
            'reserved_to',
            'animalid'
        ]
   
        
class ReservationUpdateForm(forms.ModelForm):
    reserved_date = forms.DateField()
    reserved_from = forms.TimeField()
    reserved_to = forms.TimeField()
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal',
    )
               
    class Meta:
        model = Reservation
        fields = [
            'reserved_from',
            'reserved_to',
            'animalid'
        ]
            
    
class ReservationManageForm(forms.ModelForm):
    reserved_date = forms.DateField()
    reserved_from = forms.TimeField()
    reserved_to = forms.DateField()
    approval = forms.ChoiceField(choices=[(0,'unapproved'),(1,'approved')])
    state = forms.ChoiceField(choices=[('pending','pending'),
                                      ('ongoing','ongoing'),
                                      ('finished','finished')])
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
            'reserved_from',
            'reserved_to',
            'approval',
            'state',
            'animalid',
            'volunteerid'
        ]
