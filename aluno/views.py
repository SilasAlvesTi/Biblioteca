from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Aluno


class AlunoListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Aluno


class AlunoCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Aluno
    fields = [
        "nome",
        "cadastro",
    ]
    success_url = reverse_lazy("aluno:list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy("aluno:create"))
