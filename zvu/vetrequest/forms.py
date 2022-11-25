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
    creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": "70", "rows": "8"}))
    # state = forms.ChoiceField(choices=[('pending','pending'),
    #                                   ('finished','finished')])

    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal',
        widget=forms.HiddenInput()
    )
    vetid = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='vet'),
        label='Veterinarian',
        # widget=forms.HiddenInput()
    )
               
    class Meta:
        model = Vetrequest
        fields = [
            'creation_date',
            'content',
            # 'state',
            'animalid',
            'vetid'
        ]


class VetrequestNewForm(forms.ModelForm):
    creation_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": "70", "rows": "8"}))
    # state = forms.ChoiceField(choices=[('pending','pending'),
    #                                   ('finished','finished')])
    animalid = MyModelChoiceField(
        queryset=Animal.objects.all(),
        label='Animal',
        # widget=forms.HiddenInput()
    )
    vetid = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='vet'),
        label='Veterinarian',
        # widget=forms.HiddenInput()
    )
               
    class Meta:
        model = Vetrequest
        fields = [
            'creation_date',
            'content',
            # 'state',
            'animalid',
            'vetid'
        ]

        
        
class VetrequestExamForm(forms.ModelForm):
    exam_time = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    exam_procedure = forms.ChoiceField(choices=[('vaccination','vaccination'),
                                                ('regular checkup','regular checkup'),
                                                ('other','other')])
     
    class Meta:
        model = Vetrequest
        fields = [
            'exam_time',
            'exam_procedure'
        ]


# class VetrequestNewForm(forms.ModelForm):
    
#     animalid = MyModelChoiceField(
#         queryset=Animal.objects.all(),
#         label='Animal'
#     )
    
#     vetid = forms.ModelChoiceField(
#         queryset=User.objects.filter(groups__name='vet'),
#         label='Veterinarian'
#     )
    
#     class Meta:
#         model = Vetrequest
#         fields = [
#             'state',
#             'animalid',
#             'vetid'
#         ]
