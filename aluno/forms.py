from django import forms
from django.forms import fields

from aluno import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "nome",
            "cadastro",
        ]
