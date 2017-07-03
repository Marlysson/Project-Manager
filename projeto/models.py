from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "projeto"

    def __str__(self):
        return self.nome


class Funcao(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "funcao"

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=9,decimal_places=2,null=True)
    endereco = models.OneToOneField('Endereco',on_delete=models.CASCADE)

    class Meta:
        db_table = "funcionario"

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    projeto = models.OneToOneField(Projeto,on_delete=models.CASCADE)
    membros = models.ManyToManyField(Funcionario,through='Participacao')

    class Meta:
        db_table = "equipe"


class Participacao(models.Model):
    equipe = models.ForeignKey(Equipe,on_delete=models.CASCADE,
                            related_name="participantes")
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE,
                            related_name="participacoes")
    funcao = models.OneToOneField(Funcao)

    class Meta:
        db_table = "participacao"


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

    class Meta:
        db_table = "tarefa"

    def __str__(self):
        return "{}, {}".self(self.titulo,self.status)


class Checklist(models.Model):
    descricao = models.CharField(max_length=50)
    tarefa = models.ForeignKey(Tarefa,on_delete=models.CASCADE,
                            related_name="checklists")

    def addItem(self,descricao):
        item = Item.objects.create(descricao=descricao,checklist=self)
        self.itens.add(item)

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


class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    class Meta:
        db_table = "endereco"
        
    def __str__(self):
        return "{}, {}".format(self.rua,self.bairro)