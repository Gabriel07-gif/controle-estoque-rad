"""
main.py — Arquivo principal do sistema (Gabriel)
Responsável por integrar banco.py, interface.py e utils.py.
"""

import tkinter as tk
from tkinter import messagebox

import banco
import interface
import utils


def acao_cadastrar():
    """Fluxo do botão Cadastrar:
    1. Pega valores dos Entry
    2. Valida com utils
    3. Insere com banco
    4. Registra log
    5. Atualiza Treeview
    6. Limpa campos
    """
    # TODO: Pessoa 4 — implementar
    pass


def acao_atualizar():
    """Fluxo do botão Atualizar:
    1. Verifica se há produto selecionado
    2. Pega valores dos Entry
    3. Valida com utils
    4. Atualiza com banco
    5. Registra log
    6. Atualiza Treeview
    7. Limpa campos
    """
    # TODO: Pessoa 4 — implementar
    pass


def acao_excluir():
    """Fluxo do botão Excluir:
    1. Verifica se há produto selecionado
    2. Pede confirmação com messagebox.askokcancel()
    3. Deleta com banco
    4. Registra log
    5. Atualiza Treeview
    6. Limpa campos
    """
    # TODO: Pessoa 4 — implementar
    pass


def main():
    """Função principal que inicializa a aplicação."""
    # Criar o banco de dados
    banco.criar_tabela()

    # Criar a janela principal
    root = tk.Tk()
    root.title("Controle de Estoque - RAD")
    root.geometry("800x600")
    root.resizable(True, True)

    # Montar a interface
    interface.criar_interface(root)

    # TODO: Pessoa 4 — conectar os botões às funções acima
    # Exemplo: interface.btn_cadastrar.config(command=acao_cadastrar)

    # Carregar dados iniciais no Treeview
    interface.atualizar_treeview()

    # Iniciar o loop da interface
    root.mainloop()


if __name__ == "__main__":
    main()
