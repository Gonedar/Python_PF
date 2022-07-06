from django import forms
from products.models import Tortas


class Torta_form(forms.ModelForm):
    class Meta:
        model = Tortas
        fields = '__all__'
