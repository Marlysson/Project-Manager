
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$",views.index,name="index"),
	
	url(r"^projetos$",views.projetos,name="projetos"),
	url(r"^funcionarios$",views.funcionarios,name="funcionarios"),
	url(r"^tarefas$",views.tarefas,name="tarefas"),
	url(r"^tarefa/(?P<id_tarefa>\d+)$",views.tarefa,name="tarefa"),

	url(r"^novo_projeto$",views.novo_projeto,name="novo_projeto"),
	url(r"^novo_funcionario$",views.novo_funcionario,name="novo_funcionario"),
	url(r"^nova_tarefa$",views.nova_tarefa,name="nova_tarefa"),
]
