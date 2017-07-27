from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def addEquipe(self,equipe):
        equipe.projeto = self
        equipe.save()

    class Meta:
        db_table = "projeto"

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "funcao"

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=9,decimal_places=2)
    funcao = models.ForeignKey(funcao,on_delete=models.SET_NULL)

    class Meta:
        db_table = "funcionario"

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,
                                related_name="equipes")
    membros = models.ManyToManyField(Funcionario)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "equipe"


class Tarefa(models.Model):

    STATUS = (
        (0,'A fazer'),
        (1,'Fazendo'),
        (2,'Feito'),
    )

    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    esforco = models.DurationField()
    data_conclusao = models.DateTimeField(null=True)
    status = models.CharField(max_length=1,choices=STATUS)
    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,related_name="tarefas")
    pre_requisito = models.ManyToManyField("self",
                                symmetrical=False,
                                related_name="pre_requisitos")

    def concluir(self):
        from datetime import datetime
        
        self.dataconclusao = datetime.now()
        self.status = 2

        self.save()

    class Meta:
        db_table = "tarefa"

    def __str__(self):
        return "{}, {}".self(self.titulo,self.status)


class Checklist(models.Model):
    descricao = models.CharField(max_length=50)
    tarefa = models.ForeignKey(Tarefa,on_delete=models.CASCADE,
                            related_name="checklists")

    def addItem(self,item):
        item.checklist = self
        item.save()

    class Meta:
        db_table = "checklist"

    def __str__(self):
        return self.descricao

class Item(models.Model):
    descricao = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    checklist = models.ForeignKey(Checklist,on_delete=models.CASCADE,
                                related_name="itens")

    class Meta:
        db_table = "item"

    def __str__(self):
        return "{}, {}".format(self.descricao,self.status)
