from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mapa/", views.mapa, name="mapa"),
    path("setor/novo/", views.novo_setor, name="novo_setor"),
    path("aviso/novo/", views.novo_aviso, name="novo_aviso"),
    path("contato/", views.contato, name="contato"),
]