from django import forms
from django.contrib.auth.models import User
from shelter.models import Timetable, Animal

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class TimetableForm(forms.ModelForm):
    reserved_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    reserved_from = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    reserved_to = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    is_free = forms.ChoiceField(choices=[(1,'free'),(0,'reserved')])
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal'
        )
    
    class Meta:
        model = Timetable
        fields = [
            'reserved_date',
            'reserved_from',
            'reserved_to',
            'is_free',
            'animalid'    
        ]
