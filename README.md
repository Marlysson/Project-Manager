# Project Manager

Description's project: **Implementation of a simple project manager.**

## Features

- Team management
- Tasks ( using checklists )
- Time management
- Reports

## Requirements

- Python 3.6
- [Pipenv](https://docs.pipenv.org/)

## Building the development environment


```bash
# Install dependence's and environment's library
sudo pip install pipenv
```

```bash
# Clone the repository 
git clone https://github.com/Marlysson/Project-Manager.git

# Enter the project
cd Project-Manager

# Install dependences
pipenv install

# Create and load environment variables
python contrib/env_gen.py

# Activate environment's project
pipenv shell

# Run migrations
python manage.py migrate
```

## How synchonize your fork

Read [how_to](how_to.md)

## Inicial class diagram's project

![Projeto de classes](https://github.com/Marlysson/Project-Manager/blob/master/Documenta%C3%A7%C3%A3o/Diagrama.png)

## FUNCIONALIDADES GERENCIADOR DE PROJETOS

### AUTENTICAÇÃO

	1. CADASTRO DE USUÁRIO NA PLATAFORMA
	2. LOGIN
	3. RECUPERACAO DE SENHA
	4. ALTERAÇÃO DE SENHA

### GERENCIAMENTO DA TAREFA

	5. CONTAGEM DO TEMPO DA TAREFA
		5.1. QUANTIDADE DE TEMPO DECORRIDO DESDE A ABERTURA ATÉ A CONCLUSÃO, USANDO PAUSA E PLAY NA TAREFA.
		5.2. SE VALENDO PELO HORÁRIO DE TRABALHO DO FUNCIONÁRIO

	6. ADIÇÃO DE DEPENDÊNCIA ENTRE TAREFAS
		6.1. SE INICIAR UMA TAREFA QUE TEM DEPENDÊNCIAS QUE NÃO SE INICIARAM GERAR UM ERRO
		
	7. ADICIONAR RESPONSÁVEL PELA TAREFA
	8. ADICIONAR LABELS DE IMPORTÂNCIA DA TAREFA
		8.1. PODENDO ADICIONAR O STATUS DA TAREFA
	9. DEFINIÇÃO DE PRAZOS DAS TAREFAS
	10. EFETUAR BUSCA POR NOME DAS TAREFAS

### GERENCIAMENTO DE NOTIFICAÇÕES

	11. MAPEAR EVENTOS QUE OCORREM NO SISTEMA
		-ALTERAÇÃO DE PRAZO DA TAREFA
		-ADIÇÃO DE RESPONSÁVEIS NA TAREFA
		-PRAZO DA TAREFA PRÓXIMO DE SE ESGOTAR
		-CITAÇÃO EM COMENTÁRIOS
		-REAÇÃO À COMENTÁRIOS

### TRATAMENTO DE ENGAJAMENTO DOS TIMES NOS PROJETOS ( RELATÓRIO )

	13. VISUALIZAÇÃO DE PRODUTIVIDADE DE FUNCIONÁRIO
		12.1. QUANTIDADE DE TAREFAS FEITAS POR FUNCIONÁRIO

### GERENCIAMENTO DO FLUXO DE TRABALHO

	14. CRIAÇÃO DO CONCEITO DE SPRINT E ASSOCIAÇÃO DE ALGUNS REQUISITOS DENTRO DO SPRINT
	15. GERAR RELATÓRIO DE QUANTIDADE DE TAREFAS POR SPRINTS
		15.1. QUANTAS TAREFAS EM CADA SPRINT ATRASARAM
		15.2. QUANTAS TAREFAS TERMINARAM NO TEMPO HÁBIL
		15.3. QUANTIDADE DE TAREFAS POR SPRINT

### GERENCIAMENTO DE INTERAÇÃO NA TAREFA ( SIMILAR AO GITHUB ISSUES COMMENTS )
	
	17. POSSIBILIDADE DE COMENTÁRIO NA TAREFA
	17. POSSIBILIDADE DE REAGIR AO COMENTÁRIO
		SIMILAR AO FACEBOOK REACTIONS	
	18. POSSIBILIDADE DE CITAÇÃO NOS COMENTÁRIOS
		E COM ISSO CRIAR UMA NOTIFICAÇÃO


## SEPARAÇÃO DE CONCEITOS NAS APLICAÇÕES

- AUTH
- NOTIFICATIONS
- WORKFLOW
- THREAD-COMMENTS
