# Mini Sistema de Controle de Estoque (RAD)

Sistema desktop com interface gráfica para gerenciamento de estoque, desenvolvido com Python, tkinter e SQLite seguindo a metodologia de Desenvolvimento Rápido de Aplicações (RAD).

---

## Sobre o projeto

Uma aplicação de tela única que permite cadastrar, visualizar, editar e excluir produtos do estoque de uma loja, com log de auditoria persistente em arquivo `.txt` e banco de dados relacional SQLite.

## Tecnologias

- **Python 3.10+**
- **tkinter** — Interface gráfica (GUI)
- **SQLite3** — Banco de dados relacional
- **Faker** — Geração de dados fictícios para testes

## Estrutura do projeto

```
controle-estoque-rad/
├── src/
│   ├── principal.py            # Arquivo principal (integração)
│   ├── banco.py           # Conexão e operações no banco de dados
│   ├── interface.py       # Interface gráfica com tkinter
│   └── logs.py           # Logs de auditoria e validações
├── relatorio/
│   └── relatorio_rad.pdf  # Relatório da metodologia RAD
├── estoque.db             # Banco de dados SQLite (gerado na execução)
├── log_estoque.txt        # Log de auditoria (gerado na execução)
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivos ignorados pelo Git
├── contribuirgithub.md        # Guia de contribuição da equipe
└── README.md              # Este arquivo
```

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/controle-estoque-rad.git
cd controle-estoque-rad
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
python etapas/principal.py
```

## Divisão da equipe

| Membro     | Responsabilidade         | Arquivo principal | Branch            |
|------------|--------------------------|-------------------|-------------------|
| Victoria   | Banco de dados + CRUD    | `src/banco.py`    | `feat/banco`      |
|   Paulo    | Interface gráfica        | `src/interface.py`| `feat/interface`  |
|   Juan     | Logs + Validações        | `src/utils.py`    | `feat/utils`      |
|   Gabriel  | Integração + Relatório   | `src/main.py`     | `feat/integracao` |

> Consulte o arquivo [contribuirgithub.md](contribuirgithub.md) para ver o fluxo de trabalho com Git.

## Funcionalidades

- [x] **Create** — Cadastrar produto com nome, quantidade e preço
- [x] **Read** — Listar todos os produtos em uma tabela (Treeview)
- [x] **Update** — Clicar em um produto para editar seus dados
- [x] **Delete** — Excluir produto com confirmação
- [x] **Log de auditoria** — Registro de todas as operações em `log_estoque.txt`
- [x] **Validação de dados** — Tratamento de erros com `try/except`

## Formato do log

```
[12/05/2026 14:30:15] INSERÇÃO - Produto "Monitor" (Qtd: 10) cadastrado com sucesso.
[12/05/2026 15:45:00] ATUALIZAÇÃO - Produto "Monitor" alterado (Nova Qtd: 8, Novo Preço: 850.00).
[13/05/2026 09:12:30] EXCLUSÃO - Produto "Teclado Mecânico" removido do sistema.
```

## Licença

Projeto acadêmico — uso educacional.
