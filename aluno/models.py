from django.db import models
from django.urls import reverse


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cadastro = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome
