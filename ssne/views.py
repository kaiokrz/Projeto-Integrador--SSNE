from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Setor, Aviso
from .forms import SetorForm, AvisoForm, MensagemForm, UserCreationForm

from django.db.models import Q
from .models import Aviso

def index(request):
    if request.user.is_authenticated:
        # Se for Administrador (staff ou superuser), vê TUDO
        if request.user.is_staff or request.user.is_superuser:
            avisos = Aviso.objects.all()
        
        # Se o usuário logado tiver um curso definido diretamente nele
        elif request.user.curso:
            curso_usuario = request.user.curso
            # Filtra avisos do curso do usuário OU avisos gerais (nulos ou vazios)
            avisos = Aviso.objects.filter(
                Q(curso=curso_usuario) | Q(curso__isnull=True) | Q(curso='')
            ).distinct()
            
        else:
            # Usuário logado mas sem curso definido, vê apenas os avisos gerais
            avisos = Aviso.objects.filter(Q(curso__isnull=True) | Q(curso=''))
    else:
        # Visitante não logado, vê apenas os avisos gerais
        avisos = Aviso.objects.filter(Q(curso__isnull=True) | Q(curso=''))

    context = {'avisos': avisos}
    return render(request, "ssne/index.html", context)

def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    context = {
        "form":form,
        }
    return render(request, "registration/cadastro.html", context)
    
@login_required
@permission_required("ssne.add_setor")
def novo_setor(request):
    if request.method == "POST":
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Setor cadastrado com sucesso!')
            return redirect("mapa")
    else:
        form = SetorForm()

    context = {
        "form": form,
    }
    return render(request, "ssne/form_setor.html", context)

def setor_detalhe(request, id_setor):
    context = {
        "setor": get_object_or_404(Setor, id=id_setor),
    }
    return render(request, "ssne/setor_detalhe.html", context)

@login_required
@permission_required("ssne.change_setor")
def editar_setor(request, id_setor):
    setor = get_object_or_404(Setor, id=id_setor)
    if request.method == "POST":
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Setor editado com sucesso!')
            return redirect("setor_detalhe", id_setor=setor.id)
    else:
        form = SetorForm(instance=setor)

    context = {
        "form": form,
        "is_editar": True,
    }
    return render(request, "ssne/form_setor.html", context)


@login_required
@permission_required("ssne.delete_setor")
def remover_setor(request, id_setor):
    setor = get_object_or_404(Setor, id=id_setor)
    if request.method == "POST":
        setor.delete()
        messages.success(request, 'Setor removido com sucesso!')
        return redirect("mapa")
    else:
        context = {"titulo_objeto": setor.nome}
        return render(request, "ssne/confirmar_remocao.html", context)


@login_required
@permission_required("ssne.add_aviso")
def criar_aviso(request):
    if request.method == "POST":
        form = AvisoForm(request.POST, request.FILES)
        if form.is_valid():
            aviso = form.save(commit=False)
            aviso.autor = request.user
            aviso.save()
            messages.success(request, 'Aviso publicado com sucesso!')
            return redirect("index")
    else:
        form = AvisoForm()

    context = {
        "form": form,
    }
    return render(request, "ssne/criar_aviso.html", context)


@login_required
@permission_required("ssne.change_aviso")
def editar_aviso(request, id_aviso):
    aviso = get_object_or_404(Aviso, id=id_aviso)
    if request.method == "POST":
        form = AvisoForm(request.POST, request.FILES, instance=aviso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aviso editado com sucesso!')
            return redirect("index")
    else:
        form = AvisoForm(instance=aviso)

    context = {
        "form": form,
        "is_editar": True,
    }
    return render(request, "ssne/editar_aviso.html", context)


@login_required
@permission_required("ssne.delete_aviso")
def remover_aviso(request, id_aviso):
    aviso = get_object_or_404(Aviso, id=id_aviso)
    if request.method == "POST":
        aviso.delete()
        messages.success(request, 'Aviso removido com sucesso!')
        return redirect("index")
    else:
        context = {"titulo_objeto": aviso.titulo}
        return render(request, "ssne/remover_aviso.html", context)
    
def contato(request):
    form = MensagemForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mensagem enviada com sucesso. Obrigado pela contribuição!")
        return redirect("contato")
    return render(request, "ssne/contato.html", {"form": form})

def mapa(request):
    return render(request, "ssne/mapa.html")