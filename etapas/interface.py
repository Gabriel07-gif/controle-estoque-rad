"""
interface.py — Módulo de interface gráfica (Paulo)
Responsável por toda a GUI com tkinter em tela única.
"""

import tkinter as tk
from tkinter import ttk, messagebox


# Variáveis globais dos campos do formulário
entry_nome = None
entry_quantidade = None
entry_preco = None
tree = None
produto_selecionado_id = None


def criar_interface(root):
    """Monta todos os widgets na janela principal.
    
    Args:
        root: Janela principal tk.Tk()
    
    A interface deve conter:
    - Frame superior: formulário com Entry para nome, quantidade, preço
    - Frame central: botões Cadastrar, Atualizar, Excluir, Limpar
    - Frame inferior: Treeview com colunas (ID, Nome, Quantidade, Preço)
    """
    # TODO: Pessoa 2 — implementar
    # Lembre-se: TELA ÚNICA, sem Toplevel
    pass


def preencher_formulario(event):
    """Ao clicar em um item no Treeview, preenche os campos do formulário.
    
    Args:
        event: Evento de clique do Treeview
    """
    # TODO: Pessoa 2 — implementar
    # Dica: use tree.selection() e tree.item() para pegar os dados
    pass


def limpar_campos():
    """Limpa todos os campos Entry do formulário."""
    # TODO: Pessoa 2 — implementar
    pass


def atualizar_treeview():
    """Recarrega todos os dados do banco no Treeview.
    
    Deve chamar banco.listar_produtos() e inserir no Treeview.
    """
    # TODO: Pessoa 2 — implementar
    # Dica: limpe o Treeview antes com tree.delete(*tree.get_children())
    pass
