from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.http.response import HttpResponseRedirect

from .models import Autor


class AutorListView(ListView):
    model = Autor


class AutorCreate(CreateView):
    model = Autor
    fields = [
        "nome",
    ]
    uccess_url = reverse_lazy("autor:create")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse_lazy("autor:create"))
