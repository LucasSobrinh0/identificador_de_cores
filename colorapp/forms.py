# colorapp/forms.py

from django import forms

class RGBForm(forms.Form):
    rgb = forms.CharField(label='Digite a cor em RGB', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Exemplo: 255,0,255'}))
