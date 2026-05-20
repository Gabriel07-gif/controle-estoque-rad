"""
interface.py — Módulo de interface gráfica (Paulo)
Responsável por toda a GUI com tkinter em tela única.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import banco


# Variáveis globais dos campos do formulário
entry_nome = None
entry_quantidade = None
entry_preco = None
tree = None
produto_selecionado_id = None
btn_cadastrar = None
btn_atualizar = None
btn_excluir = None
btn_limpar = None


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
    global entry_nome, entry_quantidade, entry_preco, tree
    global btn_cadastrar, btn_atualizar, btn_excluir, btn_limpar

    # Frame superior: formulário
    frame_top = ttk.Frame(root, padding=10)
    frame_top.pack(fill=tk.X)

    ttk.Label(frame_top, text="Nome:").grid(row=0, column=0, sticky=tk.W, pady=2)
    entry_nome = ttk.Entry(frame_top)
    entry_nome.grid(row=0, column=1, sticky=tk.EW, pady=2)

    ttk.Label(frame_top, text="Quantidade:").grid(row=1, column=0, sticky=tk.W, pady=2)
    entry_quantidade = ttk.Entry(frame_top)
    entry_quantidade.grid(row=1, column=1, sticky=tk.EW, pady=2)

    ttk.Label(frame_top, text="Preço:").grid(row=2, column=0, sticky=tk.W, pady=2)
    entry_preco = ttk.Entry(frame_top)
    entry_preco.grid(row=2, column=1, sticky=tk.EW, pady=2)

    frame_top.columnconfigure(1, weight=1)

    # Frame central: botões
    frame_mid = ttk.Frame(root, padding=10)
    frame_mid.pack(fill=tk.X)

    btn_cadastrar = ttk.Button(frame_mid, text="Cadastrar")
    btn_cadastrar.pack(side=tk.LEFT, padx=5)

    btn_atualizar = ttk.Button(frame_mid, text="Atualizar")
    btn_atualizar.pack(side=tk.LEFT, padx=5)

    btn_excluir = ttk.Button(frame_mid, text="Excluir")
    btn_excluir.pack(side=tk.LEFT, padx=5)

    btn_limpar = ttk.Button(frame_mid, text="Limpar", command=limpar_campos)
    btn_limpar.pack(side=tk.LEFT, padx=5)

    # Frame inferior: Treeview
    frame_bot = ttk.Frame(root, padding=10)
    frame_bot.pack(fill=tk.BOTH, expand=True)

    cols = ("id", "nome", "quantidade", "preco")
    tree = ttk.Treeview(frame_bot, columns=cols, show="headings")
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("preco", text="Preço")

    tree.column("id", width=50, anchor=tk.CENTER)
    tree.column("nome", anchor=tk.W)
    tree.column("quantidade", width=100, anchor=tk.CENTER)
    tree.column("preco", width=100, anchor=tk.E)

    vsb = ttk.Scrollbar(frame_bot, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(fill=tk.BOTH, expand=True)

    tree.bind("<<TreeviewSelect>>", preencher_formulario)



def preencher_formulario(event):
    """Ao clicar em um item no Treeview, preenche os campos do formulário.
    
    Args:
        event: Evento de clique do Treeview
    """
    global produto_selecionado_id
    sel = tree.selection()
    if not sel:
        return
    item = tree.item(sel[0])
    vals = item.get("values", [])
    if not vals:
        return
    produto_selecionado_id = vals[0]
    # Preencher campos
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, vals[1])
    entry_quantidade.delete(0, tk.END)
    entry_quantidade.insert(0, vals[2])
    entry_preco.delete(0, tk.END)
    entry_preco.insert(0, vals[3])



def limpar_campos():
    """Limpa todos os campos Entry do formulário."""
    global produto_selecionado_id
    produto_selecionado_id = None
    if entry_nome:
        entry_nome.delete(0, tk.END)
    if entry_quantidade:
        entry_quantidade.delete(0, tk.END)
    if entry_preco:
        entry_preco.delete(0, tk.END)
    try:
        tree.selection_remove(tree.selection())
    except Exception:
        pass


def atualizar_treeview():
    """Recarrega todos os dados do banco no Treeview.
    
    Deve chamar banco.listar_produtos() e inserir no Treeview.
    """
    # Recarrega dados do banco
    for r in tree.get_children():
        tree.delete(r)
    try:
        rows = banco.listar_produtos()
        for row in rows:
            # row = (id, nome, quantidade, preco)
            tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))
    except Exception:
        pass
