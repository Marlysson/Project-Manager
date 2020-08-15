from django.urls import include, path
from . import views


tarefa_patterns = [
    path("", views.tarefas, name="tarefas"),
    path("<int:id_tarefa>", views.tarefa, name="tarefa"),
    path(
        "<int:id_tarefa>/iniciar",
        views.iniciar_tarefa,
        name="iniciar_tarefa"
    ),
    path(
        "<int:id_tarefa>/pausar",
        views.pausar_tarefa,
        name="pausar_tarefa"
    ),
    path(
        "<int:id_tarefa>/concluir",
        views.concluir_tarefa,
        name="concluir_tarefa"
    ),
    path(
        "<int:id_tarefa>/deletar",
        views.deletar_tarefa,
        name="deletar_tarefa"
    ),
    path(
        "<int:id_tarefa>/comentar",
        views.comentar,
        name="comentar"
    ),
    path(
        "<int:id_tarefa>/permitido_iniciar",
        views.permissao_iniciar,
        name="permissao_iniciar"
    ),
]

urlpatterns = [
    path("", views.index, name="projetos"),
    path("funcionarios/", views.funcionarios, name="funcionarios"),
    path("novo_projeto/", views.novo_projeto, name="novo_projeto"),
    path("novo_funcionario/", views.novo_funcionario, name="novo_funcionario"),
    path("nova_tarefa/", views.nova_tarefa, name="nova_tarefa"),
    path("tarefa/", include(tarefa_patterns)),
]
