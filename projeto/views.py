from django.shortcuts import render
from django.shortcuts import redirect

from .models import Projeto

def index(request):
	return render(request,"index.html",{})

def projetos(request):
	
	projetos = Projeto.objects.all()
	
	contexto = {"projetos":projetos}

	return render(request,"projetos.html",contexto)

def criar_projeto(request):

	nome = request.POST.get("nome")
	descricao = request.POST.get("descricao")

	novo = Projeto.objects.create(nome=nome,descricao=descricao)

	return redirect("projetos")