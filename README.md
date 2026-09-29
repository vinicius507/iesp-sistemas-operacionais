# Sistemas Operacionais

Submissão para projeto da disciplina de Sistemas Operacionais da UNIESP.

O projeto consiste em uma CLI básica para demonstrar serviços do Sistema Operacional para lidar com:

- **Arquivos:** comandos para criar, ler, escrever, renomear e remover arquivos
- **Diretórios:** comandos criar e listar diretórios
- **Processos:** comandos para adquirir PID do processo atual e executar processos

## Instalação

**Requisitos:**

- Python 3.13

Para instalar usando `pip`:

```bash
$ pip install git+https://github.com/vinicius507/iesp-sistemas-operacionais
```

Usando `uv`:

```bash
$ uv tool install git+https://github.com/vinicius507/iesp-sistemas-operacionais
```

## Utilização

Ao instalar, um executável `so` é instalado:

```bash
$ so --help

 Usage: so [OPTIONS] COMMAND [ARGS]...

 Aplicação em Python construida para disciplina de sistemas operacionais

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                             │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                      │
│ --help                        Show this message and exit.                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ arquivo    Comandos para ler e manipular arquivos                                                                                   │
│ diretorio  Comandos para criar e listar diretórios                                                                                  │
│ processo   Comandos para gerenciamento de processos                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

**Exemplos:**

- **Criar arquivo:**
  ```bash
  $ so arquivo criar teste.txt
   teste.txt criado com sucesso
  ```
- **Listar diretórios**
  ```bash
  $ so diretorio listar
   .
   .git/
   .gitignore
   .python-version
   .venv/
   README.md
   pyproject.toml
   src/
   teste.txt
   uv.lock
  ```
- **Executar comando:**
  ```bash
  $ so processo executar echo "Olá, Mundo"
  $ echo Olá, Mundo
  Olá, Mundo
   processo criado com PID 210597
   processo 210597 finalizado com código 0
  ```
