from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Projeto, Funcionario, Tarefa, Comentario
from .forms import FuncionarioForm

def index(request):
	
	projetos = Projeto.objects.all()

	contexto = {"projetos":projetos}

	return render(request,"projetos.html",contexto)

def novo_projeto(request):

	nome = request.POST.get("nome")
	descricao = request.POST.get("descricao")

	novo = Projeto.objects.create(nome=nome,descricao=descricao)

	return redirect("projetos")

def funcionarios(request):

	funcionarios = Funcionario.objects.all()
	contexto = {"funcionarios":funcionarios}

	return render(request,"funcionarios.html",contexto)

def novo_funcionario(request):

	novo_funcionario = FuncionarioForm(request.POST)

	if novo_funcionario.is_valid():
		novo_funcionario.save()

	return redirect("funcionarios")

def tarefas(request):

	tarefas = Tarefa.objects.all()
	projetos = Projeto.objects.all()
	funcionarios = Funcionario.objects.all()
	
	contexto = {"tarefas":tarefas,"projetos":projetos,"funcionarios":funcionarios}

	return render(request,"tarefas.html",contexto)

def tarefa(request,id_tarefa):
	
	tarefa = Tarefa.objects.get(id=id_tarefa)

	return render(request,"tarefa.html",{"tarefa":tarefa})

	
def nova_tarefa(request):

	if request.method == 'POST':
		
		titulo = request.POST.get("titulo").capitalize()
		descricao = request.POST.get("descricao").capitalize()
		projeto = request.POST.get("projeto")
		responsavel = request.POST.get("funcionario")
		pre_requisitos = request.POST.getlist("pre_requisito")

		ids_requisitos = list(map(int,pre_requisitos))

		projeto = Projeto.objects.get(id=projeto)
		responsavel = Funcionario.objects.get(id=responsavel)

		tarefa = Tarefa(titulo=titulo,descricao=descricao,
						projeto=projeto,responsavel=responsavel)
		tarefa.save()

		if len(ids_requisitos):

			for id_requisito in ids_requisitos:
				requisito = Tarefa.objects.get(id=id_requisito)

				tarefa.pre_requisitos.add(requisito)


	return redirect("tarefas")

@require_http_methods(["POST"])
def comentar(request,id_tarefa):

	conteudo = request.POST.get("conteudo")

	tarefa = Tarefa.objects.get(id=id_tarefa)
	funcionario = get_usuario(request)

	comentario = Comentario.objects.create(conteudo=conteudo,tarefa=tarefa,
								criado_por=funcionario)

	return redirect("tarefa",id_tarefa=id_tarefa)

def iniciar_tarefa(request,id_tarefa):

	tarefa = Tarefa.objects.get(id=id_tarefa)

	pre_requisitos = tarefa.pre_requisitos.all()

	print(pre_requisitos)

	if len(pre_requisitos):

		for requisito in pre_requisitos:
			if requisito.status != 3:
				return redirect("tarefas")

		tarefa.iniciar()
	else:
		tarefa.iniciar()

	return redirect("tarefas")

def pausar_tarefa(request,id_tarefa):

	tarefa = Tarefa.objects.get(id=id_tarefa)

	tarefa.pausar()

	return redirect("tarefas")

def concluir_tarefa(request,id_tarefa):
	
	tarefa = Tarefa.objects.get(id=id_tarefa)

	tarefa.concluir()

	return redirect("tarefas")

def deletar_tarefa(request,id_tarefa):
	
	tarefa = Tarefa.objects.get(id=id_tarefa)
	tarefa.delete()

	return redirect("tarefas")


def permissao_iniciar(request,id_tarefa):

	tarefa = Tarefa.objects.get(id=id_tarefa)

	return JsonResponse({"permitido":tarefa.permitido_iniciar})


def get_usuario(request):
	return Funcionario.objects.get(id=1)

