from django.test import TestCase

from ..models import Projeto, Funcao, Funcionario, Endereco

class TestInsercoesModelos(TestCase):

    def test_deve_retornar_quantidade_de_projetos_inseridos(self):

        projeto1 = Projeto(nome="Gerenciador de Vendas").save()
        projeto2 = Projeto(nome="Implementação de API").save()

        quantidade_projetos = Projeto.objects.all().count()

        self.assertEquals(quantidade_projetos,2)
    
    def test_deve_retornar_quantidade_de_funcoes_no_banco(self):

        for funcao in ["Backend Developer","FrontEnd Developer", "Tester"]:
            funcao = Funcao.objects.create(nome=funcao)

        funcoes = Funcao.objects.all().count()

        self.assertEquals(funcoes,3)

    def test_deve_criar_um_funcionario_e_associar_um_endereco_a_ele(self):

        endereco = Endereco.objects.create(rua="Rua 1",bairro="Bairro 1",
                            cidade="Cidade 1",estado="Estado 1")

        funcionario = Funcionario(nome="Marlysson",idade=21,
                                salario=2.500,endereco=endereco)
        funcionario.save()

        funcionario_banco = Funcionario.objects.get(id=funcionario.id)

        self.assertEquals(funcionario_banco.nome,"Marlysson")