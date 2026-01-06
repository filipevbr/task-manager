
class Task:
    # Inicia o objeto Task
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

class TaskManager:
    # Inicia o objeto TaskManager
    def __init__(self):
        self.tasks = []
    
    # Inicia o metodo add_task
    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        print(f"Tarefa '{new_task.title}' adicionada com sucesso.")
    
    # Inicia o metodo list_tasks
    def list_tasks(self):
        if not self.tasks:
            print("A lista está vazia.")
            return
        
        for task in self.tasks:
            print(task)
    
    # Inicia o metodo complete_task
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Tarefa {task} concluída.")
                return
            
        print("Tarefa não encontrada.")
