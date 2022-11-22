from django import forms
from shelter.models import Animal


class AnimalForm(forms.ModelForm):
    breed = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    registration_date = forms.DateField()
    
    class Meta:
        model = Animal
        fields = [
            'breed',
            'name',
            'age',
            'registration_date'
        ]
