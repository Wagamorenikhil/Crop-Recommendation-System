from django import forms
from .models import Season, Crop

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name']

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'description']
