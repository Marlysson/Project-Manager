from django.shortcuts import render
from django.shortcuts import redirect

from .models import Projeto, Funcionario
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
		print("entrou")

	return redirect("funcionarios")