from src.tarefas import Tarefa, GerenciadorDeTarefas

def test_adicionar_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = Tarefa(1, "Entregar pacote na rota sul", "Alta")
    gerenciador.adicionar(tarefa)
    assert len(gerenciador.tarefas) == 1
    assert gerenciador.tarefas[0].prioridade == "Alta"

def test_concluir_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = Tarefa(1, "Revisar logistica")
    gerenciador.adicionar(tarefa)
    gerenciador.concluir(1)
    assert gerenciador.tarefas[0].status == "Concluido"

def test_remover_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = Tarefa(1, "Pacote cancelado")
    gerenciador.adicionar(tarefa)
    gerenciador.remover(1)
    assert len(gerenciador.tarefas) == 0