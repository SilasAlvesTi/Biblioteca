from biblioteca import forms
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Livro
from aluno.models import Aluno

# from .forms import EmprestimoForm


class LivroListView(ListView):
    model = Livro


class LivroDetailView(DetailView, forms.Form):
    model = Livro
    querry_aluno = Aluno.objects.all()
    fields = forms.ChoiceField(choices=[querry_aluno])


class LivroCreate(CreateView):
    model = Livro
    fields = [
        "titulo",
        "autor",
        "isbn",
        "resumo",
    ]
    success_url = reverse_lazy("biblioteca:list")


class LivroUpdate(UpdateView):
    model = Livro
    fields = [
        "titulo",
        "autor",
        "isbn",
        "resumo",
    ]
    success_url = reverse_lazy("biblioteca:list")


class LivroDelete(DeleteView):
    queryset = Livro.objects.all()
    success_url = reverse_lazy("biblioteca:list")


def emprestimo(request):
    querry_aluno = Aluno.objects.all()
    querry_livro = Livro.objects.all()
    return render(
        request,
        "biblioteca/emprestimo.html",
        {"querry_aluno": querry_aluno, "querry_livro": querry_livro},
    )


# def emprestimo_form(request):
#     context = {}
#     context["form"] = EmprestimoForm()
#     return render(request, "emprestimo-livro.html", context)
