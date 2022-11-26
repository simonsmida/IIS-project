from django import forms
from shelter.models import Animal
import datetime

class AnimalForm(forms.ModelForm):
    breed = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    age = forms.IntegerField(min_value=0)
    registration_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)
    image = forms.URLField(max_length=255, required=False)
    
    class Meta:
        model = Animal
        fields = [
            'breed',
            'name',
            'age',
            'registration_date',
            'image'
        ]

class AnimalHealthForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea(attrs={"cols": "70", "rows": "8"}), label='',required=False)
    
    class Meta:
        model = Animal
        fields = [
            'info'
        ]