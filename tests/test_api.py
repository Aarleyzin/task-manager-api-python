import pytest
from app import create_app # Importa a função create_app do seu arquivo __init__.py

# Fixture para criar uma instância do cliente de teste do Flask
# Uma fixture é uma função que o pytest executa antes dos testes
@pytest.fixture
def client():
    app = create_app() # Cria uma instância da sua aplicação Flask
    app.config['TESTING'] = True # Ativa o modo de teste
    with app.test_client() as client:
        yield client # Retorna o cliente de teste para os testes usarem

# Teste para o endpoint GET /tasks
def test_get_tasks(client):
    """Testa se o endpoint GET /tasks retorna uma lista e status 200."""
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, list) # Verifica se a resposta é uma lista

# Teste para o endpoint POST /tasks
def test_create_task(client):
    """Testa a criação de uma nova tarefa via POST /tasks."""
    new_task_data = {"title": "Nova Tarefa de Teste", "description": "Descrição da tarefa de teste"}
    response = client.post('/tasks', json=new_task_data)
    assert response.status_code == 201 # 201 Created
    assert response.json['title'] == "Nova Tarefa de Teste"
    assert response.json['description'] == "Descrição da tarefa de teste"
    assert 'id' in response.json # Verifica se um ID foi atribuído

# Teste para o endpoint GET /tasks/<id>
def test_get_single_task(client):
    """Testa a recuperação de uma única tarefa via GET /tasks/<id>."""
    # Primeiro, cria uma tarefa para poder buscá-la
    new_task_data = {"title": "Tarefa para Buscar", "description": "Detalhes da tarefa"}
    post_response = client.post('/tasks', json=new_task_data)
    task_id = post_response.json['id']

    get_response = client.get(f'/tasks/{task_id}')
    assert get_response.status_code == 200
    assert get_response.json['id'] == task_id
    assert get_response.json['title'] == "Tarefa para Buscar"

# Teste para o endpoint PUT /tasks/<id>
def test_update_task(client):
    """Testa a atualização de uma tarefa existente via PUT /tasks/<id>."""
    # Primeiro, cria uma tarefa para poder atualizá-la
    new_task_data = {"title": "Tarefa Antiga", "description": "Descrição Antiga"}
    post_response = client.post('/tasks', json=new_task_data)
    task_id = post_response.json['id']

    updated_task_data = {"title": "Tarefa Atualizada", "description": "Descrição Atualizada", "done": True}
    put_response = client.put(f'/tasks/{task_id}', json=updated_task_data)
    assert put_response.status_code == 200
    assert put_response.json['title'] == "Tarefa Atualizada"
    assert put_response.json['description'] == "Descrição Atualizada"
    assert put_response.json['done'] == True

# Teste para o endpoint DELETE /tasks/<id>
def test_delete_task(client):
    """Testa a exclusão de uma tarefa via DELETE /tasks/<id>."""
    # Primeiro, cria uma tarefa para poder deletá-la
    new_task_data = {"title": "Tarefa para Deletar", "description": "Será excluída"}
    post_response = client.post('/tasks', json=new_task_data)
    task_id = post_response.json['id']

    delete_response = client.delete(f'/tasks/{task_id}')
    assert delete_response.status_code == 204 # 204 No Content para sucesso na exclusão

    # Tenta buscar a tarefa deletada para confirmar que não existe mais
    get_response_after_delete = client.get(f'/tasks/{task_id}')
    assert get_response_after_delete.status_code == 404 # 404 Not Found

# Teste para verificar se uma tarefa não existente retorna 404
def test_get_non_existent_task(client):
    """Testa se a busca por uma tarefa inexistente retorna status 404."""
    response = client.get('/tasks/99999') # ID que provavelmente não existe
    assert response.status_code == 404

# Teste para verificar se a atualização de uma tarefa não existente retorna 404
def test_update_non_existent_task(client):
    """Testa se a atualização de uma tarefa inexistente retorna status 404."""
    updated_task_data = {"title": "Tarefa Inexistente", "description": "Não deveria existir", "done": True}
    response = client.put('/tasks/99999', json=updated_task_data)
    assert response.status_code == 404

# Teste para verificar se a exclusão de uma tarefa não existente retorna 404
def test_delete_non_existent_task(client):
    """Testa se a exclusão de uma tarefa inexistente retorna status 404."""
    response = client.delete('/tasks/99999')
    assert response.status_code == 404
