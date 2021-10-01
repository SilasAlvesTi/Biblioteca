from django.urls import path
from . import views

app_name = "aluno"


urlpatterns = [
    path("create/", views.AlunoCreate.as_view(), name="create"),
]
