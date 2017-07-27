
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$",views.index,name="index"),
	
	url(r"^projetos$",views.projetos,name="projetos"),
	url(r"^funcionarios$",views.funcionarios,name="funcionarios"),

	url(r"^novo_projeto$",views.novo_projeto,name="novo_projeto"),
	url(r"^novo_funcionario$",views.novo_funcionario,name="novo_funcionario"),
]
