from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome
