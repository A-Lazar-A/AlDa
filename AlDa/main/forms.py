from .models import CounterParty
from django import forms



class CounterPartyForm(forms.ModelForm):
    class Meta:
        model = CounterParty
        fields = ['Name','Hired', 'Value' ]
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Value': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'Hired': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }