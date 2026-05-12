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
    # TODO: Pessoa 3 — implementar
    # Dica: abrir arquivo com modo 'a' (append)
    # Usar datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
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
    # TODO: Pessoa 3 — implementar
    # Dica: usar .strip() para limpar espaços
    pass


def validar_quantidade(qtd: str) -> int:
    """Valida e converte a quantidade para inteiro.
    
    Args:
        qtd: Quantidade digitada pelo usuário (string do Entry)
    
    Returns:
        Quantidade como inteiro positivo
    
    Raises:
        ValueError: Se não for um número inteiro válido ou for negativo
    """
    # TODO: Pessoa 3 — implementar
    # Dica: usar try/except para capturar erro de conversão
    pass


def validar_preco(preco: str) -> float:
    """Valida e converte o preço para float.
    
    Args:
        preco: Preço digitado pelo usuário (string do Entry)
    
    Returns:
        Preço como float positivo
    
    Raises:
        ValueError: Se não for um número válido ou for negativo
    """
    # TODO: Pessoa 3 — implementar
    # Dica: aceitar tanto "10.50" quanto "10,50" (substituir vírgula por ponto)
    pass
