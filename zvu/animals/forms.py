from django import forms
from shelter.models import Animal


class AnimalForm(forms.ModelForm):
    breed = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    age = forms.IntegerField(min_value=0)
    registration_date = forms.DateField()
    info = forms.CharField(widget=forms.Textarea(attrs={"cols": "70", "rows": "8"}), label='Health record')
    
    class Meta:
        model = Animal
        fields = [
            'breed',
            'name',
            'age',
            'registration_date',
            'info'
        ]
