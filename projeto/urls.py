
from django.conf.urls import url
from . import views

urlpatterns = [
	url("^$",views.index,name="index"),
	url("^projetos$",views.projetos,name="projetos"),

	url("^criar_projeto$",views.criar_projeto,name="criar_projeto")
]