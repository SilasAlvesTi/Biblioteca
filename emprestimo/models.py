from aluno.models import Aluno
from biblioteca.models import Livro
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify, truncatechars
from django.urls import reverse


class Emprestimo(models.Model):
    data_entrega = models.DateTimeField(verbose_name="Data de Entrega")
    data_criacao = models.DateTimeField(null=True)

    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="livro")
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, related_name="aluno")

    class Meta:
        db_table = "emprestimo"

    def get_data_evento(self):
        return self.data_evento.strftime("%d/%m/%Y %H:%M Hrs")

    def get_data_input_evento(self):
        return self.data_evento.strftime("%Y-%m-%dT%H:%M")
