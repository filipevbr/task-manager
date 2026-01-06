from task_manager import TaskManager

manager = TaskManager()

def show_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Concluir")
    print("4 - Sair")

while True:
    show_menu()
    option = input("Opção: ").strip()
    match option:
        case "1":
            title = input("\nTarefa: ").strip()
            description = input("Descrição: ").strip()
            manager.add_task(title, description)
        case "2":
            manager.list_tasks()
        case "3":
            manager.list_tasks()
            try:
                id_int = int(input("Digite o ID da tarefa: "))
                manager.complete_task(id_int)
            except ValueError:
                print("\nDigite apenas números.")
        case "4":
            break
        case _:
            print("Verifique a opção escolhida.")    