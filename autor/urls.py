from django.urls import path
from . import views

app_name = "autor"


urlpatterns = [
    path("create/", views.AutorCreate.as_view(), name="create"),
]
