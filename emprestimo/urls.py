from django.urls import path
from . import views

app_name = "emprestimo"


urlpatterns = [
    path(
        "listar-emprestimos/",
        views.EmprestimoList.as_view(),
        name="listar-emprestimos",
    ),
    path(
        "listar-emprestimos/cadastrar-emprestimo/",
        views.EmprestimoCreate.as_view(),
        name="cadastrar-emprestimo",
    ),
    path(
        "listar-emprestimos/editar/emprestimo/<int:pk>/",
        views.EmprestimoUpdate.as_view(),
        name="editar-emprestimo",
    ),
    path(
        "listar-emprestimos/excluir/emprestimo/<int:pk>/",
        views.EmprestimoDelete.as_view(),
        name="excluir-emprestimo",
    ),
]
