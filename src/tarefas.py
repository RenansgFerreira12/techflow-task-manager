class Tarefa:
    def __init__(self, id, descricao, prioridade="Normal"):
        self.id = id
        self.descricao = descricao
        self.status = "A Fazer"
        self.prioridade = prioridade # Mudança de escopo adicionada aqui!

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)
        return True

    def concluir(self, id):
        for t in self.tarefas:
            if t.id == id:
                t.status = "Concluido"
                return True
        return False