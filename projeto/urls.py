
from django.conf.urls import url
from . import views

urlpatterns = [

	url(r"^login/$",views.logar,name="login"),
	url(r"^logout/$",views.deslogar,name="logout"),
	url(r"^cadastrar/$",views.cadastrar,name="cadastrar"),

	url(r"^$",views.index,name="projetos"),

	url(r"^funcionarios$",views.funcionarios,name="funcionarios"),
	url(r"^tarefas$",views.tarefas,name="tarefas"),
	url(r"^tarefa/(?P<id_tarefa>\d+)$",views.tarefa,name="tarefa"),

	url(r"^novo_projeto$",views.novo_projeto,name="novo_projeto"),
	url(r"^novo_funcionario$",views.novo_funcionario,name="novo_funcionario"),
	url(r"^nova_tarefa$",views.nova_tarefa,name="nova_tarefa"),

	url(r"^tarefa/(?P<id_tarefa>\d+)/iniciar$",views.iniciar_tarefa,name="iniciar_tarefa"),
	url(r"^tarefa/(?P<id_tarefa>\d+)/pausar$",views.pausar_tarefa,name="pausar_tarefa"),
	url(r"^tarefa/(?P<id_tarefa>\d+)/concluir$",views.concluir_tarefa,name="concluir_tarefa"),
	url(r"^tarefa/(?P<id_tarefa>\d+)/deletar$",views.deletar_tarefa,name="deletar_tarefa"),

	url(r"^tarefa/(?P<id_tarefa>\d+)/comentar/$",views.comentar,name="comentar"),

	url(r"^tarefa/(?P<id_tarefa>\d+)/permitido_iniciar/$",views.permissao_iniciar,name="permissao_iniciar"),
]

