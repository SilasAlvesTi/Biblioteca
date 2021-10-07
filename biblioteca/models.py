from aluno.models import Aluno
from autor.models import Autor
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify, truncatechars
from django.urls import reverse


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    resumo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True, null=True)
    atualizado = models.DateTimeField(auto_now_add=True, null=True)
    isbn = models.CharField(max_length=13, null=True)

    class Meta:
        db_table = "livro"

    def save(self):

        self.slug = slugify(self.titulo)

        super(Livro, self).save()

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        return reverse("biblioteca:detail", kwargs={"slug": self.slug})
