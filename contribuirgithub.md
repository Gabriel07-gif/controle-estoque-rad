# Guia de contribuição

Este documento explica como cada membro da equipe deve trabalhar no projeto usando Git e GitHub.

---

## Configuração inicial (uma vez só)

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/controle-estoque-rad.git
cd controle-estoque-rad
```

### 2. Configure seu nome e e-mail no Git

```bash
git config user.name "Seu Nome"
git config user.email "seu@email.com"
```

---

## Fluxo de trabalho diário

### Passo 1 — Sempre atualize antes de começar

```bash
git checkout main
git pull origin main
```

### Passo 2 — Crie (ou volte para) sua branch

Na primeira vez:

```bash
git checkout -b feat/banco       # Pessoa 1
git checkout -b feat/interface   # Pessoa 2
git checkout -b feat/utils       # Pessoa 3
git checkout -b feat/integracao  # Pessoa 4
```

Nas vezes seguintes, se a branch já existe:

```bash
git checkout feat/banco
git merge main    # Traz as atualizações da main para sua branch
```

### Passo 3 — Trabalhe e faça commits pequenos

Edite seu arquivo, salve, e depois:

```bash
git add src/banco.py                          # Adiciona o arquivo modificado
git commit -m "Cria função inserir_produto"   # Descreve o que fez
```

Regras para mensagens de commit:
- Comece com verbo no presente: "Cria", "Adiciona", "Corrige", "Remove"
- Seja específico: "Adiciona validação de preço negativo" ao invés de "Arruma coisas"
- Máximo ~70 caracteres

### Passo 4 — Envie para o GitHub

```bash
git push origin feat/banco   # Substitua pelo nome da sua branch
```

### Passo 5 — Abra um Pull Request (PR)

1. Acesse o repositório no GitHub
2. Clique no botão **"Compare & pull request"** que aparece
3. Escreva um título claro (ex: "Adiciona CRUD completo do banco de dados")
4. Descreva o que foi feito
5. Clique em **"Create pull request"**
6. Aguarde a revisão da Pessoa 4 (integradora)

---

## Ordem de merges recomendada

Para evitar conflitos, sigam esta ordem:

```
1º  feat/banco      → main   (Pessoa 1 - banco de dados)
2º  feat/utils      → main   (Pessoa 3 - logs e validações)
3º  feat/interface  → main   (Pessoa 2 - interface gráfica)
4º  feat/integracao → main   (Pessoa 4 - integração final)
```

As Pessoas 1 e 3 podem trabalhar ao mesmo tempo porque mexem em arquivos diferentes.

A Pessoa 2 deve esperar o merge das Pessoas 1 e 3 para poder importar as funções reais.

---

## Resolvendo conflitos

Se ao fazer `git merge main` aparecer um conflito:

1. Abra o arquivo com conflito — ele terá marcações assim:
   ```
   <<<<<<< HEAD
   seu código
   =======
   código da main
   >>>>>>> main
   ```
2. Edite o arquivo mantendo o código correto
3. Remova as marcações (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Salve, faça `git add` e `git commit`

---

## Contrato de funções (combinar antes de codar)

Para evitar retrabalho, todos devem seguir estes nomes de funções:

### banco.py (Pessoa 1)

```python
def criar_tabela()
def inserir_produto(nome: str, quantidade: int, preco: float) -> bool
def listar_produtos() -> list
def atualizar_produto(id: int, nome: str, quantidade: int, preco: float) -> bool
def deletar_produto(id: int) -> bool
```

### utils.py (Pessoa 3)

```python
def registrar_log(tipo: str, mensagem: str)
def validar_nome(nome: str) -> str          # retorna nome limpo ou levanta ValueError
def validar_quantidade(qtd: str) -> int      # retorna int ou levanta ValueError
def validar_preco(preco: str) -> float       # retorna float ou levanta ValueError
```

### interface.py (Pessoa 2)

```python
def criar_interface(root)          # monta todos os widgets na janela
def preencher_formulario(event)    # clique no Treeview preenche os campos
def limpar_campos()                # reseta todos os Entry
def atualizar_treeview()           # recarrega os dados no Treeview
```

---

## Comandos úteis

| Ação                              | Comando                              |
|-----------------------------------|--------------------------------------|
| Ver status dos arquivos           | `git status`                         |
| Ver histórico de commits          | `git log --oneline`                  |
| Ver branches                      | `git branch`                         |
| Trocar de branch                  | `git checkout nome-da-branch`        |
| Descartar mudanças locais         | `git checkout -- nome-do-arquivo`    |
| Ver diferenças antes de commitar  | `git diff`                           |
