from django import forms
from shelter.models import Vetrequest, Animal
from django.contrib.auth.models import User

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

# class VetrequestForm(forms.ModelForm):
#     creation_date = forms.DateField()
#     reserved_from = forms.DateField()
#     reserved_to = forms.DateField()
#     animalid = MyModelChoiceField(
#         queryset=Animal.objects.all(),
#         label='Animal',
#         widget=forms.HiddenInput()
#     )
               
#     class Meta:
#         model = Vetrequest
#         fields = [
#             'creation_date',
#             'reserved_from',
#             'reserved_to',
#             'animalid'
#         ]
        
# class VetrequestUpdateForm(forms.ModelForm):
#     creation_date = forms.DateField()
#     reserved_from = forms.DateField()
#     reserved_to = forms.DateField()
#     animalid = MyModelChoiceField(
#         queryset=Animal.objects.all(),
#         label='Animal',
#     )
               
#     class Meta:
#         model = Vetrequest
#         fields = [
#             'creation_date',
#             'reserved_from',
#             'reserved_to',
#             'animalid'
#         ]
            
    
class VetrequestForm(forms.ModelForm):
    creation_date = forms.DateField()
    content = forms.TextInput()
    state = forms.CharField(max_length=255)
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal'
    )
    vetid = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='vet'),
        label='Veterinarian'
    )
               
    class Meta:
        model = Vetrequest
        fields = [
            'creation_date',
            'content',
            'state',
            'animalid',
            'vetid'
        ]
