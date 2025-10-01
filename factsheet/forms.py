# factsheet/forms.py
from django import forms
from .models import (
    Factsheet, AnnexureII, AnnexureIII,
    TransitCamp, Approval, ConstructionStatus, StopWork
)

class FactsheetForm(forms.ModelForm):
    class Meta:
        model = Factsheet
        fields = '__all__'


class AnnexureIIForm(forms.ModelForm):
    class Meta:
        model = AnnexureII
        fields = '__all__'


class AnnexureIIIForm(forms.ModelForm):
    class Meta:
        model = AnnexureIII
        fields = '__all__'


class TransitCampForm(forms.ModelForm):
    class Meta:
        model = TransitCamp
        fields = '__all__'


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = '__all__'


class ConstructionStatusForm(forms.ModelForm):
    class Meta:
        model = ConstructionStatus
        fields = '__all__'


class StopWorkForm(forms.ModelForm):
    class Meta:
        model = StopWork
        fields = '__all__'
