# 📋 Task Manager CLI

Um gerenciador de tarefas pessoal, robusto e simples, desenvolvido em Python. O objetivo deste projeto é aplicar conceitos avançados de Orientação a Objetos e Arquitetura de Software em uma aplicação de linha de comando.

---

## 🚀 Funcionalidades Atuais (MVP)

* **Adicionar Tarefa:** Criação de tarefas com título e descrição.
* **Listagem Inteligente:** Visualização do status (Pendente `[ ]` ou Concluído `[X]`).
* **Conclusão de Tarefa:** Busca linear por ID para marcar tarefas como feitas.
* **Interface CLI:** Menu interativo via terminal com tratamento de erros.
* **Persistência de Dados (JSON):** Salvar tarefas para não perder dados ao fechar.

---

## 🛠️ Arquitetura

O projeto segue o princípio de **Separação de Responsabilidades**:
* `task_manager.py`: O **Core** (Backend). Contém as regras de negócio e gestão de estado.
* `main.py`: A **Interface** (Frontend). Gerencia a interação com o usuário e validação de inputs.

## 🔮 Roadmap (Funcionalidades Futuras)

* [ ] **Delete:** Remover tarefas indesejadas.
* [ ] **Edição:** Alterar título/descrição de tarefas existentes.
* [ ] **Filtros:** Listar apenas "Pendentes" ou "Concluídas".

---

## 💻 Como Usar

1.  Certifique-se de ter o **Python 3.10** (ou superior) instalado.

2.  Clone este repositório:
    ```bash
    git clone https://github.com/filipevbr/task-manager.git
    ```

3.  Navegue até o diretório do projeto:
    ```bash
    cd task-manager
    ```

4.  **Execute o sistema:**
    ```bash
    python src/main.py
    ```

---

## 👨‍💻 Autor

* **Filipe Vaz**
      *(Estudante de Análise e Desenvolvimento de Sistemas - PUCPR)*