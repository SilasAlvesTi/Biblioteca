from biblioteca import forms
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Emprestimo

###Ze fez apartir daqui


class EmprestimoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Emprestimo
    template_name = "listar-emprestimos.html"


# class LivroDetailView(LoginRequiredMixin,DetailView, forms.Form):
#   login_url = reverse_lazy('login')
#  model = Emprestimo
# querry_aluno = Aluno.objects.all()
# fields = forms.ChoiceField(choices=[querry_aluno])


class EmprestimoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    model = Emprestimo
    fields = [
        "data_entrega",
        "data_criacao",
        "livro",
        "aluno",
    ]
    template_name = "cadastrar-emprestimo.html"
    success_url = reverse_lazy("emprestimo:listar-emprestimos")


class EmprestimoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Emprestimo
    fields = [
        "data_entrega",
        "data_criacao",
        "livro",
        "aluno",
    ]
    template_name = "cadastrar-emprestimo.html"
    success_url = reverse_lazy("emprestimo:listar-emprestimos")


class EmprestimoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = Emprestimo
    template_name = "excluir-emprestimo.html"
    success_url = reverse_lazy("emprestimo:listar-emprestimos")


# def emprestimo(request):
#   querry_aluno = Aluno.objects.all()
#  querry_livro = Livro.objects.all()
# return render(
#    request,
#   "biblioteca/emprestimo.html",
#  {"querry_aluno": querry_aluno, "querry_livro": querry_livro},
# )


# def emprestimo_form(request):
#     context = {}
#     context["form"] = EmprestimoForm()
#     return render(request, "emprestimo-livro.html", context)
