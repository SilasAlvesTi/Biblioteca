from biblioteca import forms
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from biblioteca.models import Livro
from aluno.models import Aluno

# from .forms import EmprestimoForm
class LivroListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Livro


class LivroDetailView(LoginRequiredMixin, DetailView, forms.Form):
    login_url = reverse_lazy("login")
    model = Livro
    querry_aluno = Aluno.objects.all()
    fields = forms.ChoiceField(choices=[querry_aluno])


class LivroCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    model = Livro
    fields = [
        "titulo",
        "autor",
        "isbn",
        "resumo",
    ]
    success_url = reverse_lazy("biblioteca:list")


class LivroUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Livro
    fields = [
        "titulo",
        "autor",
        "isbn",
        "resumo",
    ]
    success_url = reverse_lazy("biblioteca:list")


class LivroDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    queryset = Livro.objects.all()
    success_url = reverse_lazy("biblioteca:list")
