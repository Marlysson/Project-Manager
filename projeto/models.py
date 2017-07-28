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

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=9,decimal_places=2)
    cargo = models.CharField(max_length=100)

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

    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    data_conclusao = models.DateTimeField(null=True)
    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,related_name="tarefas")
    horario_de_inicio_atual = models.DateTimeField(null=True)
    duracao_total = models.DurationField(null=True,default=0)
    responsavel = models.ForeignKey(Funcionario,null=True)
    pre_requisito = models.ManyToManyField("self",null=True,
                                symmetrical=False,
                                related_name="pre_requisitos")

    def iniciar(self):

        from datetime import datetime

        self.horario_inicio_atual = datetime.now()

        self.save()

    def concluir(self):
        from datetime import datetime
        
        self.dataconclusao = datetime.now()
        self.duracao_total += datetime.now() - self.dataconclusao

        self.save()

    def pausar(self):

        from datetime import datetime
        agora = datetime.now()

        self.duracao_total += agora - self.horario_inicio_atual

        self.save()

    class Meta:
        db_table = "tarefa"

    def __str__(self):
        return "{}, {}".format(self.titulo,self.status)


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

class Comentario(models.Model):

    conteudo = models.TextField()
    criado_por = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comentario"