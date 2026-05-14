import sqlite3  # importa a biblioteca para trabalharmos com banco de dados SQLite
from faker import Faker # importa a biblioteca que vai gerar dados falsos para popular o banco nos testes

def criar_banco():
    with sqlite3.connect("estoque.db") as conn:# abre ou cria o arquivo estoque.db, o with garante que a conexão feche mesmo se der erro
        cursor = conn.cursor() # cria o cursor que é o ponteiro que executa os comandos dentro do nosso banco de dados
        # cria a tabela só se ela se ela não existir, assim o programa pode rodar várias vezes sem dar erro  na linha abaixo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                nome       TEXT    NOT NULL,
                quantidade INTEGER NOT NULL,
                preco      REAL    NOT NULL,
                categoria  TEXT    NOT NULL
            )
        """)
        conn.commit() # confirma e salva as mudanças feitas no banco
        

def inserir_produto(nome, quantidade, preco, categoria):
    try: # se der qualquer erro no banco, ele captura e mostra a mensagem em vez de travar o programa
        with sqlite3.connect("estoque.db") as conn:
            cursor = conn.cursor() 
            # inserindo as linhas da tabela abaixo
            # espaços reservados para evitar problemas de segurança do SQL INJECTION NA LINHA ABAIXO
            cursor.execute("""
                INSERT INTO produtos (nome, quantidade, preco, categoria)
                VALUES (?, ?, ?, ?)
            """, (nome, quantidade, preco, categoria))
            conn.commit()
    except sqlite3.Error as e:  # se der qualquer erro no banco, ele captura e mostra a mensagem em vez de travar o programa
        print(f"Erro ao inserir produto: {e}")
        
def listar_produtos():
    try:
        with sqlite3.connect("estoque.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos") # seleciona todos os registros da tabela
            return cursor.fetchall() # retorna ttodos os resultados como uma lista de tuplas
    except sqlite3.Error as e:
        print(f"Erro ao listar produtos: {e}")
        return [] # se der erro retorna uma lista vazia em vez de none evitando problemas na interface da segunda pessoa
    
def atualizar_produto(id, nome, quantidade, preco, categoria):
    try:
        with sqlite3.connect("estoque.db") as conn:
            cursor = conn.cursor()
            # indica que vamos atualizar/mudar os dados que já temos na tabela NA INHA ABAIXO
            cursor.execute("""
                UPDATE produtos
                SET nome = ?, quantidade = ?, preco = ?, categoria = ? # defini quais campos vão ser alterados e com quais valores
                WHERE id = ? # IMPORTANTE: garante que só o produto com o ID certo vai ser atualizado
            """, (nome, quantidade, preco, categoria, id)) # o id vai por ultimo porque ele aparece por ultimo na query/Sql
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar produto: {e}")
        
def deletar_produto(id):
    try:
        with sqlite3.connect("estoque.db") as conn:
            cursor = conn.cursor()
            # IMPORTANTE: garante que só o produto com o ID certo vai ser deletado NA LINHA ABAIXO
            cursor.execute("""
                DELETE FROM produtos # Remove um registro da tabela
                WHERE id = ?
            """, (id,)) # necessário colocar a vírgula para indicar que é uma tupla, no Python, uma tupla com um único elemento precisa da vírgula para ser reconhecida como tupla
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar produto: {e}")
        
def popular_banco():
    fake = Faker("pt_BR") # Gera dados falsos em portugues
    categorias = ["Eletrônicos", "Periféricos", "Informática", "Acessórios", "Escritório"]
    
    try:
        with sqlite3.connect("estoque.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM produtos") # Conta quantos produtos já existem na tabela
            total = cursor.fetchone()[0]
            
            if total == 0: # só prenche os dados se a tabela estiver vazia, evitando duplicar os dados
                for _ in range(10): # cria os 10 produtos falsos
                    nome = fake.word().capitalize()
                    quantidade = fake.random_int(min=1, max=100)
                    preco = round(fake.random_number(digits=3) / 10, 2)
                    categoria = fake.random_element(categorias) # métodos do fake para criar palavras números inteiros e elementos aleatórios da lista
                    inserir_produto(nome, quantidade, preco, categoria)
                print("Banco populado com dados fictícios!")
            else:
                print("Banco já possui dados, pulando população.")
    except sqlite3.Error as e:
        print(f"Erro ao popular banco: {e}")
        
if __name__ == "__main__":
    criar_banco()
    popular_banco()
    