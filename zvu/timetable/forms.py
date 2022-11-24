from django import forms
from django.contrib.auth.models import User
from shelter.models import Timetable


class TimetableForm(forms.ModelForm):
    day = forms.CharField(max_length=255)
    time_from = forms.TimeField()
    time_to = forms.TimeField()
    is_free = forms.ChoiceField(choices=[(0,'free'),(1,'reserved')])

    class Meta:
        model = Timetable
        fields = [
            'day',
            'time_from',
            'time_to',
            'is_free'
        ]
