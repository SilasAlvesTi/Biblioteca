from django import forms
from django.db.models.query_utils import Q
from django.forms import fields

from biblioteca.models import Livro
from aluno.models import Aluno


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            "titulo",
            "autor",
            "resumo",
            "isbn",
        ]


# class EmprestimoForm(forms.ModelForm):
#     querry_aluno = Aluno.objects.all()
#     querry_livro = Livro.objects.all()
#     class Meta:
#         model = Aluno
#         fields = [
#             "nome",
#         ]


# class EmprestimoForm(forms.Form):
#     aluno_querry = Aluno.objects.all()
#     aluno_nomes = forms.ModelChoiceField(choices=[aluno_querry])
#     # livro_querry = Livro.objects.all()
#     # livro_titulos = forms.ChoiceField(choices=[livro_querry])
