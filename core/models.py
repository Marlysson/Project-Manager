from django.db import models
from django.utils import timezone

from datetime import timedelta


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def addEquipe(self, equipe):
        equipe.projeto = self
        equipe.save()

    class Meta:
        db_table = "projeto"

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=9, decimal_places=2)
    cargo = models.CharField(max_length=100)

    class Meta:
        db_table = "funcionario"

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="equipes"
    )
    membros = models.ManyToManyField(Funcionario)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "equipe"


class Tarefa(models.Model):

    STATUS_TAREFA = (
        (0, "ABERTA"),
        (1, "TRABALHANDO"),
        (2, "PAUSADA"),
        (3, "CONCLUíDA")
    )

    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    data_conclusao = models.DateTimeField(null=True)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )
    horario_de_inicio_atual = models.DateTimeField(null=True)
    duracao_total = models.DurationField(
        null=True,
        default=timedelta(seconds=0)
    )
    status = models.CharField(max_length=1, default=0, choices=STATUS_TAREFA)
    responsavel = models.ForeignKey(Funcionario, null=True,on_delete=models.SET_NULL)
    pre_requisito = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="pre_requisitos"
    )

    @property
    def is_open(self):
        return self.status == '0'

    @property
    def is_running(self):
        return self.status == '1'

    @property
    def is_paused(self):
        return self.status == '2'

    @property
    def is_done(self):
        return self.status == '3'

    def iniciar(self):

        self.horario_de_inicio_atual = timezone.now()
        self.status = 1

        self.save()

    def concluir(self):

        self.dataconclusao = timezone.now()
        self.duracao_total += timezone.now() - self.dataconclusao
        self.status = 3

        self.save()

    def pausar(self):

        diferenca = timezone.now() - self.horario_de_inicio_atual
        self.duracao_total += diferenca

        self.status = 2
        self.save()

    @property
    def permitido_iniciar(self):

        for requisito in self.pre_requisitos:
            if requisito.status != 3:
                return False
        return True

    class Meta:
        db_table = "tarefa"

    def __str__(self):
        return "{}, {}".format(self.titulo, self.status)


class Checklist(models.Model):
    descricao = models.CharField(max_length=50)
    tarefa = models.ForeignKey(
        Tarefa,
        on_delete=models.CASCADE,
        related_name="checklists"
    )

    def addItem(self, item):
        item.checklist = self
        item.save()

    class Meta:
        db_table = "checklist"

    def __str__(self):
        return self.descricao


class Item(models.Model):
    descricao = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    checklist = models.ForeignKey(
        Checklist,
        on_delete=models.CASCADE,
        related_name="itens"
    )

    class Meta:
        db_table = "item"

    def __str__(self):
        return "{}, {}".format(self.descricao, self.status)


class Comentario(models.Model):

    conteudo = models.TextField()
    tarefa = models.ForeignKey(
        Tarefa,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    criado_por = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comentario"
        ordering = ['-criado_em']
