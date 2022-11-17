from django import forms
from shelter.models import Animal


class AnimalForm(forms.ModelForm):
    druh = forms.CharField(max_length=255)
    meno = forms.CharField(max_length=255)
    vek = forms.IntegerField()
    datum_registracie = forms.DateField()
    
    class Meta:
        model = Animal
        fields = [
            'druh',
            'meno',
            'vek',
            'datum_registracie'
        ]
