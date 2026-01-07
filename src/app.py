import flet as ft
from task_manager import TaskManager

def main(page: ft.Page):
    manager = TaskManager()  # Cria uma instancia do TaskManager importado do task_manager.py

    # Configuracoes da janela
    page.title = "Task Manager"
    page.scroll = "adaptive"
    page.window_width = 390
    page.window_height = 844
    page.window_resizable = False
    page.bgcolor = ft.Colors.BLUE_GREY_900

    page.add(ft.Text(value="Minhas Tarefas", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE))

    tasks_view = ft.Column()
    input_task = ft.TextField(label="O que precisa ser feito?", bgcolor=ft.Colors.BLUE_GREY_800, color=ft.Colors.WHITE, expand=True)

    # Funcao que arruma as colunas
    def render_tasks():
        tasks_view.controls.clear()  # Limpa o conteúdo da coluna (Acessa usando .controls)
        if not manager.tasks:
            # Adiciona um aviso DENTRO da coluna (.controls.append)
            tasks_view.controls.append(ft.Text("Nenhuma tarefa encontrada.", color=ft.Colors.GREY))
        else:
            for task in manager.tasks:
                text = ft.Text(value=f"{task.id}. {task.title}", size=18, color=ft.Colors.WHITE)  # Cria o texto
                tasks_view.controls.append(text)  # Adiciona o texto DENTRO da coluna (.controls.append)
        page.update()

    # Funcao de clique do botao
    def add_clicked(event):
        if input_task.value:
            manager.add_task(input_task.value, "Via App")  # Salva no backend
            input_task.value = ""  # Limpa o campo visual
            render_tasks()

    # Cria o botao para adicionar tarefas
    button_add = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)

    # Montagem da tela
    input_row = ft.Row(controls=[input_task, button_add])

    page.add(input_row)
    page.add(tasks_view)

    render_tasks()

if __name__ == "__main__":
    ft.app(main)