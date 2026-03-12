# Gerenciador de Tarefas com API RESTful em Python

Um projeto de nível intermediário que implementa uma API RESTful simples para gerenciar tarefas. Desenvolvido em Python utilizando o framework Flask e o ORM Flask-SQLAlchemy para persistência de dados em um banco de dados SQLite.

Este projeto demonstra a criação de endpoints CRUD (Create, Read, Update, Delete) para uma entidade de `Task`, oferecendo uma base sólida para o desenvolvimento de aplicações back-end.

## Funcionalidades

* **Listar todas as tarefas:** `GET /tasks`
* **Obter uma tarefa específica:** `GET /tasks/<id>`
* **Criar uma nova tarefa:** `POST /tasks`
* **Atualizar uma tarefa existente:** `PUT /tasks/<id>`
* **Deletar uma tarefa:** `DELETE /tasks/<id>`

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Flask:** Microframework web para a construção da API.
* **Flask-SQLAlchemy:** ORM (Object-Relational Mapper) para interação com o banco de dados.
* **SQLite:** Banco de dados leve e embutido (configurável para outros bancos).
* **python-dotenv:** Para gerenciar variáveis de ambiente.

## ⚙️ Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python 3.8+ instalado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/aarleyzin/task-manager-api-python.git
cd task-manager-api-python
```

### 2. Criar e Ativar o Ambiente Virtual

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto, baseado no `.env.example`:
