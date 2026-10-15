from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mapa/", views.mapa, name="mapa"),
    path("setor/novo/", views.novo_setor, name="novo_setor"),
    path("aviso/novo/", views.criar_aviso, name="criar_aviso"),
    path("aviso/<int:id_aviso>/editar", views.editar_aviso, name="editar_aviso"),
    path('aviso/<int:id_aviso>/remover/', views.remover_aviso, name='remover_aviso'),
    path("contato/", views.contato, name="contato"),

    path(
        "conta/senha/", 
        auth_views.PasswordChangeView.as_view(
            template_name="registration/alterar_senha.html",
            success_url="/conta/senha/sucesso/"
        ), 
        name="alterar_senha"
    ),
    path(
        "conta/senha/sucesso/", 
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/senha_alterada.html"
        ), 
        name="password_change_done"
    ),
]