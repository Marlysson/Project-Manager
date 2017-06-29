from django.db import models


class Projeto(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Funcao(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	idade = models.IntegerField()
	endereco = models.OneToOneField('Endereco',on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


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
	pre_requisito = models.ManyToManyField("self",related_name="pre_requisitos")

	def __str__(self):
		return "{}, {}".self(self.titulo,self.status)


class Checklist(models.Model):
	descricao = models.CharField(max_length=50)
	porcentagem_concluida = models.FloatField()
	tarefa = models.ForeignKey(Tarefa,on_delete=models.CASCADE,related_name="checklists")


class Item(models.Model):
	descricao = models.CharField(max_length=50)
	status = models.BooleanField(default=False)
	checklist = models.ForeignKey(Checklist,on_delete=models.CASCADE,related_name="itens")

	def __str__(self):
		return "{}, {}".format(self.descricao,self.status)


class Endereco(models.Model):
	rua = models.CharField(max_length=50)
	bairro = models.CharField(max_length=50)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)

	def __str__(self):
		return "{}, {}".format(self.rua,self.bairro)