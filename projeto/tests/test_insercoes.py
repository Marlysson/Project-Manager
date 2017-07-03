from django.test import TestCase
from datetime import timedelta

from ..models import Projeto, Funcao, Funcionario, \
                    Endereco, Tarefa, Checklist

class TestInsercoesModelos(TestCase):

    def setUp(self):
        self.projeto = Projeto.objects.create(nome="Gateway Pagamentos")
        self.funcao = Funcao.objects.create(nome="Backend Developer").save()
        self.funcionario = Funcionario(nome="Marlysson",idade=21,
                                salario=2.500)

        self.tarefa = Tarefa.objects.create(titulo="Implementar Gateway de serviço",
                        descricao="Lorem ipsum",
                        esforco=timedelta(days=4),
                        status=2,projeto=self.projeto)   

    def test_deve_retornar_quantidade_de_projetos_inseridos(self):

        projeto2 = Projeto(nome="Implementação de API").save()

        quantidade_projetos = Projeto.objects.all().count()

        self.assertEquals(quantidade_projetos,2)
    
    def test_deve_retornar_quantidade_de_funcoes_criadas(self):

        for funcao in ["Backend Developer","FrontEnd Developer", "Tester"]:
            funcao = Funcao.objects.create(nome=funcao)

        funcoes = Funcao.objects.all().count()

        self.assertEquals(funcoes,4)

    def test_deve_criar_um_funcionario_e_associar_um_endereco_a_ele(self):

        endereco = Endereco.objects.create(rua="Rua 1",bairro="Bairro 1",
                            cidade="Cidade 1",estado="Estado 1")

        self.funcionario.endereco = endereco
        self.funcionario.save()

        funcionario_banco = Funcionario.objects.get(id=self.funcionario.id)

        self.assertEquals(funcionario_banco.nome,"Marlysson")

    def test_criar_uma_checklist_para_uma_tarefa(self):
        
        checklist = Checklist.objects.create(descricao="Primeiros passos para integrar api",tarefa=self.tarefa)
        checklist.addItem("Fazer busca inicial de requisitos")
        checklist.addItem("Concluir requisitos prioritários")
        checklist.addItem("Enviar para o cliente")

        checklist_inserida = Checklist.objects.get(id=1)

        self.assertEquals(checklist_inserida.descricao,"Primeiros passos para integrar api")

        self.assertEquals(checklist_inserida.itens.count(),3)
