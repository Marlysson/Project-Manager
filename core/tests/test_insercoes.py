from django.test import TestCase
from datetime import timedelta

from ..models import Projeto, Funcao, Funcionario, \
                    Endereco, Tarefa, Checklist, \
                    Equipe, Participacao, Item

class TestInsercoesModelos(TestCase):

    def setUp(self):
        self.projeto = Projeto.objects.create(nome="Gateway Pagamentos")
        self.tarefa = Tarefa.objects.create(titulo="Implementar Gateway de serviço",
                        descricao="Lorem ipsum",
                        esforco=timedelta(days=4),
                        status=2,projeto=self.projeto)   

        self.endereco = Endereco.objects.create(rua="Rua 1",bairro="Bairro 1",
                    cidade="Cidade 1",estado="Estado 1")

    def test_deve_retornar_quantidade_de_projetos_inseridos(self):

        projeto2 = Projeto(nome="Implementação de API").save()

        quantidade_projetos = Projeto.objects.all().count()

        self.assertEquals(quantidade_projetos,2)
    
    def test_deve_retornar_quantidade_de_funcoes_criadas(self):

        for funcao in ["Backend Developer","FrontEnd Developer", "Tester"]:
            funcao = Funcao.objects.create(nome=funcao)

        funcoes = Funcao.objects.all().count()

        self.assertEquals(funcoes,3)

    def test_deve_criar_um_funcionario_e_associar_um_endereco_a_ele(self):

        funcionario = Funcionario.objects.create(nome="Marlysson",idade=21,
                                salario=2.500,endereco=self.endereco)

        funcionario_banco = Funcionario.objects.get(id=funcionario.id)

        self.assertEquals(funcionario_banco.nome,"Marlysson")

    def test_criar_uma_checklist_com_itens_para_uma_tarefa(self):
        
        checklist = Checklist.objects.create(descricao="Primeiros passos para integrar api",tarefa=self.tarefa)

        item1 = Item(descricao="Fazer busca inicial de requisitos")
        item2 = Item(descricao="Concluir requisitos prioritários")
        item3 = Item(descricao="Enviar para o cliente")

        for item in [item1,item2,item3]:
            checklist.addItem(item)

        checklist_inserida = Checklist.objects.get(id=1)

        self.assertEquals(checklist_inserida.descricao,"Primeiros passos para integrar api")

        self.assertEquals(checklist_inserida.itens.count(),3)

    def test_deve_criar_uma_equipe_para_um_projeto_associando_seus_participantes(self):

        equipe = Equipe.objects.create(nome="Desenvolvimento",projeto=self.projeto)

        funcao_backend = Funcao.objects.create(nome="Backend Developer")
        funcao_frontend = Funcao.objects.create(nome="FrontEnd Developer")

        funcionario_marlysson = Funcionario.objects.create(nome="Marlysson",idade=21,
                                salario=2.500,endereco=self.endereco)

        endereco_2 = Endereco.objects.create(rua="Rua 2",bairro="Bairro 2",
            cidade="Cidade 2",estado="Estado 2")

        funcionario_marcelo = Funcionario.objects.create(nome="Marcelo",idade=20,
                                salario=2.600,endereco=endereco_2)

        marlysson = {
            "equipe":equipe,
            "funcionario":funcionario_marlysson,
            "funcao":funcao_backend
        }

        marcelo = {
            "equipe":equipe,
            "funcionario":funcionario_marcelo,
            "funcao":funcao_frontend
        }

        participacao_1 = Participacao.objects.create(**marlysson)
        participacao_2 = Participacao.objects.create(**marcelo)

        equipe = Equipe.objects.get(id=1)

        self.assertEquals(equipe.participantes.count(),2)

    def test_deve_associar_varias_equipes_ao_mesmo_projeto(self):

        marketing = Equipe(nome="Marketing")
        desenvolvimento = Equipe(nome="Desenvolvimento")

        self.projeto.addEquipe(marketing)
        self.projeto.addEquipe(desenvolvimento)

        projeto = Projeto.objects.get(id=self.projeto.id)
        
        self.assertEquals(projeto.equipes.count(),2)

    def test_deve_retornar_a_quantidade_de_membros_no_projeto_envolvendo_todas_as_equipes_dele(self):

        equipe = Equipe.objects.create(nome="Desenvolvimento",projeto=self.projeto)

        funcao_backend = Funcao.objects.create(nome="Backend Developer")
        funcao_frontend = Funcao.objects.create(nome="FrontEnd Developer")

        funcionario_marlysson = Funcionario.objects.create(nome="Marlysson",idade=21,
                                salario=2.500,endereco=self.endereco)

        endereco_2 = Endereco.objects.create(rua="Rua 2",bairro="Bairro 2",
            cidade="Cidade 2",estado="Estado 2")

        funcionario_marcelo = Funcionario.objects.create(nome="Marcelo",idade=20,
                                salario=2.600,endereco=endereco_2)

        marlysson = {
            "equipe":equipe,
            "funcionario":funcionario_marlysson,
            "funcao":funcao_backend
        }

        marcelo = {
            "equipe":equipe,
            "funcionario":funcionario_marcelo,
            "funcao":funcao_frontend
        }

        participacao_1 = Participacao.objects.create(**marlysson)
        participacao_2 = Participacao.objects.create(**marcelo)

        participacao = Participacao.objects.filter(equipe__projeto=self.projeto.id).count()

        self.assertEquals(participacao,2)
