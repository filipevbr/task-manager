import json

class Task:
    # Inicia o objeto Tarefa
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    # Cria um retorno de string formatada
    def __str__(self):
        if self.completed:
            status = "[X]"
        else:
            status = "[ ]"

        return f"{status} {self.id} - {self.title}"
    
    # Funcao para transformar em dicionario
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
    
    # Funcao para receber um dicionario -- ao usar staticmethod e possivel receber sem ter um objeto (tarefa) criado
    @staticmethod
    def from_dict(data):
        task = Task(data["id"], data["title"], data["description"])
        task.completed = data["completed"]
        return task

class TaskManager:
    # Inicia o objeto Gerenciador de Tarefas
    def __init__(self):
        self.tasks = []
        self.load_from_file()  # Carrega os arquivos salvos ao iniciar

    # Funcao para adicionar tarefas
    def add_task(self, title, description):
        if not self.tasks:
            task_id = 1
        else:
            task_id = self.tasks[-1].id + 1  # Pega a ultima tarefa da lista e acessa o .id dela

        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)

        self.save_to_file()
        return f"Tarefa '{title}' adicionada."
    
    # Funcao para listar as tarefas
    def list_tasks(self):
        if not self.tasks:
            print("A lista está vazia.")
            return
        
        for task in self.tasks:
            print(task)

    # Funcao para deletar as tarefas
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)

                self.save_to_file()
                return "Tarefa excluida."
    
        return "Erro: Não foi possível excluir a tarefa."
    
    # Funcao para atualizar as tarefas
    def update_task(self, task_id, new_title):
        for task in self.tasks:
            if task.id == task_id:
                task.title = new_title

                self.save_to_file()
                return True
            
        return None
        
    # Funcao para salvar em um arquivo
    def save_to_file(self):
        temp_list = []
        for task in self.tasks:
            temp_list.append(task.to_dict())
        
        with open("tasks.json", "w") as file:
            json.dump(temp_list, file, indent=4)
    
    # Funcao para carregar o arquivo salvo
    def load_from_file(self):
        try:
            with open("tasks.json", "r") as file:
                data_list = json.load(file)  # Faz a leitura do arquivo e transforma em dicionario
                for data in data_list:  # Converte cada dicionario em um Objeto (tarefa)
                    task = Task.from_dict(data)
                    self.tasks.append(task)
        
        except FileNotFoundError:
            pass  

    # Funcao para alternar o status das tarefas
    def toggle_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed # Alterna o estado atual da tarefa

                self.save_to_file()
                return task.completed  # Retorna o status alterado da tarefa
            
        return None