"""
banco.py — Módulo de banco de dados (Victoria)
Responsável por todas as operações CRUD no SQLite.
"""

import sqlite3

NOME_BANCO = "estoque.db"


def criar_tabela():
    """Cria a tabela de produtos caso não exista."""
    conn = sqlite3.connect(NOME_BANCO)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def inserir_produto(nome: str, quantidade: int, preco: float) -> bool:
    """Insere um novo produto no banco de dados.
    
    Args:
        nome: Nome do produto
        quantidade: Quantidade em estoque
        preco: Preço unitário
    
    Returns:
        True se inserido com sucesso, False caso contrário
    """
    try:
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
            (nome, quantidade, preco),
        )
        conn.commit()
        return True
    except sqlite3.Error:
        return False
    finally:
        try:
            conn.close()
        except Exception:
            pass


def listar_produtos() -> list:
    """Retorna todos os produtos cadastrados.
    
    Returns:
        Lista de tuplas (id, nome, quantidade, preco)
    """
    try:
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error:
        return []
    finally:
        try:
            conn.close()
        except Exception:
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
    try:
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produtos SET nome = ?, quantidade = ?, preco = ? WHERE id = ?",
            (nome, quantidade, preco, id),
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        try:
            conn.close()
        except Exception:
            pass


def deletar_produto(id: int) -> bool:
    """Remove um produto do banco de dados.
    
    Args:
        id: ID do produto a ser removido
    
    Returns:
        True se removido com sucesso, False caso contrário
    """
    try:
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        try:
            conn.close()
        except Exception:
            pass


def popular_dados_teste(n: int = 10):
    """Popula o banco com dados fictícios usando Faker.
    
    Args:
        n: Número de produtos a gerar (padrão: 10)
    """
    try:
        from faker import Faker

        fake = Faker("pt_BR")
        categorias = ["Geral"]
        conn = sqlite3.connect(NOME_BANCO)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        if total == 0:
            for _ in range(n):
                nome = fake.word().capitalize()
                quantidade = fake.random_int(min=1, max=100)
                preco = round(fake.random_number(digits=3) / 10, 2)
                cursor.execute(
                    "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                    (nome, quantidade, preco),
                )
            conn.commit()
    except Exception:
        pass
    finally:
        try:
            conn.close()
        except Exception:
            pass
