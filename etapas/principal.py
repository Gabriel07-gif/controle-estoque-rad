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
    try:
        nome = interface.entry_nome.get()
        quantidade = interface.entry_quantidade.get()
        preco = interface.entry_preco.get()

        nome = utils.validar_nome(nome)
        quantidade = utils.validar_quantidade(quantidade)
        preco = utils.validar_preco(preco)

        ok = banco.inserir_produto(nome, quantidade, preco)
        if ok:
            utils.registrar_log("INSERÇÃO", f'Produto "{nome}" (Qtd: {quantidade}) cadastrado com sucesso.')
            interface.atualizar_treeview()
            interface.limpar_campos()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Falha ao inserir produto no banco.")
    except ValueError as e:
        messagebox.showerror("Erro de validação", str(e))
    except Exception as e:
        messagebox.showerror("Erro", str(e))


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
    try:
        prod_id = interface.produto_selecionado_id
        if not prod_id:
            messagebox.showwarning("Atenção", "Selecione um produto para atualizar.")
            return

        nome = interface.entry_nome.get()
        quantidade = interface.entry_quantidade.get()
        preco = interface.entry_preco.get()

        nome = utils.validar_nome(nome)
        quantidade = utils.validar_quantidade(quantidade)
        preco = utils.validar_preco(preco)

        ok = banco.atualizar_produto(prod_id, nome, quantidade, preco)
        if ok:
            utils.registrar_log("ATUALIZAÇÃO", f'Produto ID {prod_id} atualizado para "{nome}" (Qtd: {quantidade}).')
            interface.atualizar_treeview()
            interface.limpar_campos()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")
        else:
            messagebox.showerror("Erro", "Falha ao atualizar produto.")
    except ValueError as e:
        messagebox.showerror("Erro de validação", str(e))
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def acao_excluir():
    """Fluxo do botão Excluir:
    1. Verifica se há produto selecionado
    2. Pede confirmação com messagebox.askokcancel()
    3. Deleta com banco
    4. Registra log
    5. Atualiza Treeview
    6. Limpa campos
    """
    try:
        prod_id = interface.produto_selecionado_id
        if not prod_id:
            messagebox.showwarning("Atenção", "Selecione um produto para excluir.")
            return

        ok = messagebox.askokcancel("Confirmar", "Confirma exclusão do produto selecionado?")
        if not ok:
            return

        sucesso = banco.deletar_produto(prod_id)
        if sucesso:
            utils.registrar_log("EXCLUSÃO", f'Produto ID {prod_id} removido.')
            interface.atualizar_treeview()
            interface.limpar_campos()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Falha ao excluir produto.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


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
    interface.btn_cadastrar.config(command=acao_cadastrar)
    interface.btn_atualizar.config(command=acao_atualizar)
    interface.btn_excluir.config(command=acao_excluir)

    # Carregar dados iniciais no Treeview
    interface.atualizar_treeview()

    # Iniciar o loop da interface
    root.mainloop()


if __name__ == "__main__":
    main()
