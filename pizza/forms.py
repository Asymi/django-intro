from django import forms
from .models import Pizza

class NewPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'tastiness', 'base', 'eater']

class EatPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = []