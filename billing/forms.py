from django import forms
from .models import ModelWala

class FormWala(forms.ModelForm):
    class Meta:
        model=ModelWala
        fields='__all__'
        
