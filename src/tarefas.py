class Tarefa:
    def __init__(self, id, descricao, prioridade="Normal"):
        self.id = id
        self.descricao = descricao
        self.status = "A Fazer"
        self.prioridade = prioridade

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

    def listar(self):
        return self.tarefas

    def remover(self, id):
        self.tarefas = [t for t in self.tarefas if t.id != id]
        return True