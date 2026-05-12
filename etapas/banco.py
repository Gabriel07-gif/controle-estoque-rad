"""
banco.py — Módulo de banco de dados (Victoria)
Responsável por todas as operações CRUD no SQLite.
"""

import sqlite3

NOME_BANCO = "estoque.db"


def criar_tabela():
    """Cria a tabela de produtos caso não exista."""
    # TODO: Pessoa 1 — implementar
    # Campos sugeridos: id (INTEGER PRIMARY KEY AUTOINCREMENT),
    #                   nome (TEXT NOT NULL),
    #                   quantidade (INTEGER NOT NULL),
    #                   preco (REAL NOT NULL)
    pass


def inserir_produto(nome: str, quantidade: int, preco: float) -> bool:
    """Insere um novo produto no banco de dados.
    
    Args:
        nome: Nome do produto
        quantidade: Quantidade em estoque
        preco: Preço unitário
    
    Returns:
        True se inserido com sucesso, False caso contrário
    """
    # TODO: Pessoa 1 — implementar
    pass


def listar_produtos() -> list:
    """Retorna todos os produtos cadastrados.
    
    Returns:
        Lista de tuplas (id, nome, quantidade, preco)
    """
    # TODO: Pessoa 1 — implementar
    pass


def atualizar_produto(id: int, nome: str, quantidade: int, preco: float) -> bool:
    """Atualiza os dados de um produto existente.
    
    Args:
        id: ID do produto a ser atualizado
        nome: Novo nome
        quantidade: Nova quantidade
        preco: Novo preço
    
    Returns:
        True se atualizado com sucesso, False caso contrário
    """
    # TODO: Pessoa 1 — implementar
    pass


def deletar_produto(id: int) -> bool:
    """Remove um produto do banco de dados.
    
    Args:
        id: ID do produto a ser removido
    
    Returns:
        True se removido com sucesso, False caso contrário
    """
    # TODO: Pessoa 1 — implementar
    pass


def popular_dados_teste(n: int = 10):
    """Popula o banco com dados fictícios usando Faker.
    
    Args:
        n: Número de produtos a gerar (padrão: 10)
    """
    # TODO: Pessoa 1 — implementar com Faker
    # from faker import Faker
    # fake = Faker('pt_BR')
    pass
