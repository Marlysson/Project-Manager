from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import FuncionarioForm
from .models import Projeto, Funcionario, Tarefa, Comentario


@login_required
def index(request):
    projetos = Projeto.objects.all()
    contexto = {"projetos": projetos}
    return render(request, "projetos.html", contexto)


@login_required
def novo_projeto(request):
    nome = request.POST.get("nome")
    descricao = request.POST.get("descricao")
    novo = Projeto.objects.create(nome=nome, descricao=descricao)
    return redirect("projetos")


@login_required
def funcionarios(request):
    funcionarios = Funcionario.objects.all()
    contexto = {"funcionarios": funcionarios}
    return render(request, "funcionarios.html", contexto)


@login_required
def novo_funcionario(request):
    novo_funcionario = FuncionarioForm(request.POST)
    if novo_funcionario.is_valid():
        novo_funcionario.save()
    return redirect("funcionarios")


@login_required
def tarefas(request):
    tarefas = Tarefa.objects.all()
    projetos = Projeto.objects.all()
    funcionarios = Funcionario.objects.all()

    contexto = {
        "tarefas": tarefas,
        "projetos": projetos,
        "funcionarios": funcionarios
    }

    return render(request, "tarefas.html", contexto)


@login_required
def tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    return render(request, "tarefa.html", {"tarefa": tarefa})


@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo").capitalize()
        descricao = request.POST.get("descricao").capitalize()
        projeto = request.POST.get("projeto")
        responsavel = request.POST.get("funcionario")
        pre_requisitos = request.POST.getlist("pre_requisito")
        ids_requisitos = list(map(int, pre_requisitos))
        projeto = Projeto.objects.get(id=projeto)
        responsavel = Funcionario.objects.get(id=responsavel)

        tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            projeto=projeto,
            responsavel=responsavel
        )
        tarefa.save()

        if len(ids_requisitos):
            for id_requisito in ids_requisitos:
                requisito = Tarefa.objects.get(id=id_requisito)
                tarefa.pre_requisitos.add(requisito)

    return redirect("tarefas")


@require_http_methods(["POST"])
def comentar(request, id_tarefa):
    conteudo = request.POST.get("conteudo")
    tarefa = Tarefa.objects.get(id=id_tarefa)
    funcionario = get_usuario(request)
    Comentario.objects.create(
        conteudo=conteudo,
        tarefa=tarefa,
        criado_por=funcionario
    )
    return redirect("tarefa", id_tarefa=id_tarefa)


@login_required
def iniciar_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    pre_requisitos = tarefa.pre_requisitos.all()

    if len(pre_requisitos):
        for requisito in pre_requisitos:
            if requisito.status != 3:
                messages.info(request,'Esta tarefa possui pré-requisitos, conclua-os primeiro.')
    else:
        tarefa.iniciar()

    return redirect("tarefas")


def pausar_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    tarefa.pausar()
    return redirect("tarefas")


def concluir_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    tarefa.concluir()
    return redirect("tarefas")


def deletar_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    tarefa.delete()
    return redirect("tarefas")


def permissao_iniciar(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    return JsonResponse({"permitido": tarefa.permitido_iniciar})


def get_usuario(request):
    return Funcionario.objects.get(id=1)

