from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mapa/", views.mapa, name="mapa"),
    path("setor/novo/", views.novo_setor, name="novo_setor"),
    path("aviso/novo/", views.criar_aviso, name="criar_aviso"),
    path("aviso/<int:id_aviso>/editar", views.editar_aviso, name="editar_aviso"),
    path('aviso/<int:id_aviso>/remover/', views.remover_aviso, name='remover_aviso'),
    path("contato/", views.contato, name="contato"),
]