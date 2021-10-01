from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.http.response import HttpResponseRedirect

from .models import Aluno


class AlunoListView(ListView):
    model = Aluno


class AlunoCreate(CreateView):
    model = Aluno
    fields = [
        "nome",
        "cadastro",
    ]
    uccess_url = reverse_lazy("aluno:list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy("aluno:create"))
