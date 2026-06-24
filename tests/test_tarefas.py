from src.tarefas import Tarefa, GerenciadorDeTarefas

def test_adicionar_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = Tarefa(1, "Entregar pacote na rota sul", "Alta")
    gerenciador.adicionar(tarefa)
    assert len(gerenciador.tarefas) == 1
    assert gerenciador.tarefas[0].prioridade == "Alta" # Teste da nova feature

def test_concluir_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = Tarefa(1, "Revisar logistica")
    gerenciador.adicionar(tarefa)
    sucesso = gerenciador.concluir(1)
    assert sucesso == True
    assert gerenciador.tarefas[0].status == "Concluido"