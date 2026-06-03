"""
utils.py — Módulo de utilitários (Juan)
Responsável pelo log de auditoria e validação de dados.
"""

from datetime import datetime

ARQUIVO_LOG = "log_estoque.txt"


def registrar_log(tipo: str, mensagem: str):
    """Registra uma operação no arquivo de log.

    Args:
        tipo: Tipo da operação ("INSERÇÃO", "ATUALIZAÇÃO" ou "EXCLUSÃO")
        mensagem: Descrição detalhada da operação
    """
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
    linha = f"{timestamp} {tipo} - {mensagem}\n"
    try:
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
            f.write(linha)
    except Exception:
        pass


def validar_nome(nome: str) -> str:
    if nome is None:
        raise ValueError("Nome vazio")
    valor = nome.strip()
    if not valor:
        raise ValueError("Nome vazio")
    return valor


def validar_quantidade(qtd: str) -> int:
    try:
        valor = int(qtd)
    except Exception:
        raise ValueError("Quantidade deve ser um número inteiro")
    if valor < 0:
        raise ValueError("Quantidade não pode ser negativa")
    return valor


def validar_preco(preco: str) -> float:
    if preco is None:
        raise ValueError("Preço inválido")
    texto = preco.replace(",", ".").strip()
    try:
        valor = float(texto)
    except Exception:
        raise ValueError("Preço deve ser um número")
    if valor < 0:
        raise ValueError("Preço não pode ser negativo")
    return valor
