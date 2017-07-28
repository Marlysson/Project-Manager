from django.shortcuts import render
from django.shortcuts import redirect

from .models import Projeto, Funcionario, Tarefa
from .forms import FuncionarioForm

def index(request):
	return render(request,"index.html",{})

def projetos(request):
	
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
	pass
	
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