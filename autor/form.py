from django import forms
from django.forms import fields

from autor import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            "Nome",
        ]
