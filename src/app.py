import flet as ft
from task_manager import TaskManager

def main(page: ft.Page):
    manager = TaskManager()  # Cria uma instancia do TaskManager importado do task_manager.py
    editing_task_id = None  # Guarda o ID que esta sendo editado
    edit_field = ft.TextField(label="Novo Título", expand=True)
 
    def save_edit(e):
        if edit_field.value:
            manager.update_task(editing_task_id, edit_field.value )
            edit_dialog.open = False
            render_tasks()
            page.update()

    edit_dialog = ft.AlertDialog(
        title=ft.Text("Editar Tarefa"),  # Título da janela
        content=edit_field,              # O campo de texto vai no conteúdo
        actions=[                        # Lista de botões de ação
            ft.TextButton("Salvar", on_click=save_edit)
        ]
    )

    page.overlay.append(edit_dialog)  

    # Configuracoes da janela
    page.title = "Task Manager"
    page.scroll = "adaptive"
    page.window_width = 390
    page.window_height = 844
    page.window_resizable = False
    page.padding = 20
    page.bgcolor = ft.Colors.GREY_900
    page.window_always_on_top = True

    page.add(ft.Text(value="To Do", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE))

    tasks_view = ft.Column()
    input_task = ft.TextField(label="O que precisa ser feito?", bgcolor=ft.Colors.GREY_800, color=ft.Colors.WHITE, expand=True)
    
    # Funcao do botao adicionar tarefas
    def add_clicked(e):
        if input_task.value:
            manager.add_task(input_task.value, "Via App")  # Salva no backend
            input_task.value = ""  # Limpa o campo visual
            render_tasks()
    
    # Funcao do botao deletar tarefas
    def delete_clicked(e):
        task_id = e.control.data
        manager.delete_task(task_id)
        render_tasks()

    def edit_clicked(e):
        nonlocal editing_task_id
        editing_task_id = e.control.data

        for task in manager.tasks:
            if task.id == editing_task_id:
                edit_field.value = task.title

        edit_dialog.open = True
        page.update()

    # Funcao do check box
    def toggle_clicked(e):
        task_id = e.control.data
        manager.toggle_task(task_id)
        render_tasks()

    # Funcao que arruma as colunas
    def render_tasks():
        tasks_view.controls.clear()  # Limpa o conteúdo da coluna (Acessa usando .controls)
        if not manager.tasks:
            # Adiciona um aviso DENTRO da coluna (.controls.append)
            tasks_view.controls.append(ft.Text("Nenhuma tarefa adicionada.", color=ft.Colors.GREY))
        else:
            for task in manager.tasks:
                button_del = ft.IconButton(ft.Icons.DELETE, ft.Colors.RED_500, data=task.id, on_click=delete_clicked)  # Cria o botao de deletar
                button_edit = ft.IconButton(ft.Icons.EDIT, ft.Colors.BLUE, data=task.id, on_click=edit_clicked)  # Cria o botao de editar              
                check_box = ft.Checkbox(label=f"{task.title}", value=task.completed, data=task.id, on_change=toggle_clicked)  # Cria o checkbox
                row = ft.Row(controls=[check_box, button_edit, button_del], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)  # Linha que adiciona o texto e botao de del
                tasks_view.controls.append(row)

        page.update()

    # Cria o botao para adicionar tarefas
    button_add = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)

    # Montagem da tela
    input_row = ft.Row(controls=[input_task, button_add])  # Linha que adiciona o input da tarefa e o botao de add

    page.add(input_row)
    page.add(tasks_view)

    render_tasks()

if __name__ == "__main__":
    ft.app(target=main)