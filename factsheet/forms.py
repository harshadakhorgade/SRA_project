from django import forms
from .models import Factsheet

class FactsheetForm(forms.ModelForm):
    class Meta:
        model = Factsheet
        fields = '__all__'
        widgets = {
            'date_of_acceptance': forms.DateInput(attrs={'type': 'date'}),
            'certification_date': forms.DateInput(attrs={'type': 'date'}),
        }
