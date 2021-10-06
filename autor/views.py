from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Autor


class AutorListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Autor


class AutorCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = [
        "nome",
    ]
    uccess_url = reverse_lazy("autor:create")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy("autor:create"))
