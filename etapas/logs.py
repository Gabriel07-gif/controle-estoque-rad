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
    
    Formato esperado no arquivo:
        [DD/MM/AAAA HH:MM:SS] TIPO - Mensagem
    
    Exemplo:
        [05/05/2026 14:30:15] INSERÇÃO - Produto "Monitor" (Qtd: 10) cadastrado com sucesso.
    """
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
    linha = f"{timestamp} {tipo} - {mensagem}\n"
    try:
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
            f.write(linha)
    except Exception:
        # Não propagar erro de log para a interface
        pass


def validar_nome(nome: str) -> str:
    """Valida e limpa o nome do produto.
    
    Args:
        nome: Nome digitado pelo usuário
    
    Returns:
        Nome limpo (sem espaços extras)
    
    Raises:
        ValueError: Se o nome estiver vazio após limpeza
    """
    if nome is None:
        raise ValueError("Nome vazio")
    valor = nome.strip()
    if not valor:
        raise ValueError("Nome vazio")
    return valor


def validar_quantidade(qtd: str) -> int:
    """Valida e converte a quantidade para inteiro.
    
    Args:
        qtd: Quantidade digitada pelo usuário (string do Entry)
    
    Returns:
        Quantidade como inteiro positivo
    
    Raises:
        ValueError: Se não for um número inteiro válido ou for negativo
    """
    try:
        valor = int(qtd)
    except Exception:
        raise ValueError("Quantidade deve ser um número inteiro")
    if valor < 0:
        raise ValueError("Quantidade não pode ser negativa")
    return valor


def validar_preco(preco: str) -> float:
    """Valida e converte o preço para float.
    
    Args:
        preco: Preço digitado pelo usuário (string do Entry)
    
    Returns:
        Preço como float positivo
    
    Raises:
        ValueError: Se não for um número válido ou for negativo
    """
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
