# 📋 Task Manager

Um gerenciador de tarefas pessoal, robusto e simples, desenvolvido em Python. O objetivo deste projeto é aplicar conceitos avançados de Orientação a Objetos e Arquitetura de Software, oferecendo uma Interface Gráfica moderna.

---

## 🛠️ Arquitetura

O projeto segue o princípio de **Separação de Responsabilidades**:
* `src/task_manager.py`: O **Core** (Backend/Model). Contém as regras de negócio, gestão de estado e persistência JSON.
* `src/app.py`: A **Interface GUI** (View/Controller). Gerencia a interface gráfica e eventos do usuário usando Flet.

---

## 🚀 Funcionalidades Atuais (MVP)

* **Adicionar Tarefa:** Criação rápida de tarefas com título.
* **Listagem Visual:** Visualização clara das tarefas em uma interface estilo mobile.
* **Conclusão de Tarefa:** Checkbox interativo para marcar/desmarcar tarefas.
* **Exclusão de Tarefa:** Botão interativo (Lixeira) para remover tarefas permanentemente.
* **Persistência de Dados (JSON):** Sistema de Auto-Save/Load para manter os dados salvos no disco.
* **Interface GUI:** Interface gráfica responsiva simulando app mobile (via **Flet**).

## 🔮 Roadmap (Funcionalidades Futuras)

* [ ] **Edição:** Alterar título/descrição de tarefas existentes (Sprint 15).
* [ ] **Filtros:** Ver apenas "Pendentes" ou "Concluídas".

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

5.  **Execute o App:**
    ```bash
    python src/app.py
    ```

---

## 👨‍💻 Autor

* **Filipe Vaz**
      *(Estudante de Análise e Desenvolvimento de Sistemas - PUCPR)*