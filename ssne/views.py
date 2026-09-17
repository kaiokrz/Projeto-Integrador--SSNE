from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Setor, Aviso
from .forms import SetorForm, AvisoForm

def index(request): 
    return render(request, "ssne/index.html")

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
def novo_aviso(request):
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
    return render(request, "ssne/form_aviso.html", context)


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
    return render(request, "ssne/form_aviso.html", context)


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
        return render(request, "ssne/confirmar_remocao.html", context)