from django.urls import path
from . import views

app_name = "biblioteca"


urlpatterns = [
    path("", views.LivroListView.as_view(), name="list"),
    path("create/", views.LivroCreate.as_view(), name="create"),
    # path("emprestimo/", views.emprestimo, name="emprestimo"),
    # path("emprestimo-livro/", views.emprestimo_form, name="emprestimo"),
    path("update/<int:pk>/", views.LivroUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.LivroDelete.as_view(), name="delete"),
    path("<slug:slug>/", views.LivroDetailView.as_view(), name="detail"),
]
