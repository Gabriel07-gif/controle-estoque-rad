from datetime import datetime

#Função responsável por registrar logs no arquivo "log_estoque.txt"
def registro_log(tipo, mensagem):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log_estoque.txt", "a", encoding="utf-8") as logs_file:
        logs_file.write(f"{timestamp} - {tipo.upper()}: {mensagem}\n")


#Funções de validação dos campos do produto
#Strip para remover espaços
def validacao_nome_produto(nome: str):
    nome = nome.strip()
    if not nome:
        raise ValueError("O nome do produto não pode ser vazio.")
    return nome
    


def validacao_preco(preco: str):
    try:
        preco = preco.replace(",", ".")  #substitui vírgula por ponto
        preco = float(preco)
    except ValueError:
        raise ValueError("Número inválido.")
    
    if preco <= 0:
       raise ValueError("O preço do produto não pode ser negativo.")
    
    return preco



def validacao_quantidade(quantidade: str):
    try:
        quantidade = int(quantidade)
        
    except ValueError:
        raise ValueError("Quantidade inválida.")
    
    if quantidade < 0:
        raise ValueError("A quantidade do produto não pode ser negativa.")
    
    return quantidade

 
if __name__ == "__main__":
    #Criação do arquivo "log_estoque.txt"
    registro_log("info", "Sistema iniciado.")


    