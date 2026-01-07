# 📋 Task Manager

Um gerenciador de tarefas pessoal, robusto e simples, desenvolvido em Python. O objetivo deste projeto é aplicar conceitos avançados de Orientação a Objetos e Arquitetura de Software, oferecendo tanto uma interface CLI quanto uma Interface Gráfica moderna.

---

## 🚀 Funcionalidades Atuais (MVP)

* **Adicionar Tarefa:** Criação de tarefas com título e descrição.
* **Listagem Inteligente:** Visualização do status (Pendente `[ ]` ou Concluído `[X]`).
* **Conclusão de Tarefa:** Busca linear por ID para marcar tarefas como feitas.
* **Persistência de Dados (JSON):** Sistema de Auto-Save/Load para manter os dados salvos no disco.
* **Múltiplas Interfaces:**
    * **CLI:** Menu interativo via terminal com tratamento de erros.
    * **GUI (Mobile):** Interface gráfica responsiva simulando app mobile (via **Flet**).

---

## 🛠️ Arquitetura

O projeto segue o princípio de **Separação de Responsabilidades** (MVC):
* `src/task_manager.py`: O **Core** (Backend/Model). Contém as regras de negócio, gestão de estado e persistência JSON.
* `src/main.py`: A **Interface CLI** (Terminal). Gerencia a interação textual.
* `src/app.py`: A **Interface GUI** (Visual). Gerencia a interface gráfica usando o framework Flet.

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

4.  **Instale as dependências:**
    ```bash
    pip install flet
    ```

5.  **Execute o sistema:**
    * **Para versão Visual (Recomendado):**
      ```bash
      python src/app.py
      ```
    * **Para versão Terminal:**
      ```bash
      python src/main.py
      ```

---

## 👨‍💻 Autor

* **Filipe Vaz**
      *(Estudante de Análise e Desenvolvimento de Sistemas - PUCPR)*