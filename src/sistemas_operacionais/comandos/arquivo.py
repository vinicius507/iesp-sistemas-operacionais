import os
from os.path import dirname
from pathlib import Path
from typing import Annotated

import typer
from rich import print

from sistemas_operacionais import console

app = typer.Typer(help="Comandos para ler e manipular arquivos")


@app.command("criar")
def criar(arquivo: Annotated[Path, typer.Argument()]):
    """
    Cria um arquivo vazio no caminho especificado
    """
    try:
        with open(arquivo, "w"):
            console.success(f"[bold]{arquivo}[/bold] criado com sucesso")
    except PermissionError:
        raise console.error("você não possui permissão para criar o arquivo")
    except FileNotFoundError:
        raise console.error(f"caminho não existente {dirname(arquivo)}")
    except Exception as exc:
        raise console.error(f"não foi possível criar o arquivo: {exc!s}")


@app.command("escrever")
def escrever(
    arquivo: Annotated[Path, typer.Argument()],
    conteudo: Annotated[str, typer.Argument()],
):
    """
    Escreve conteúdo em um arquivo no caminho especificado
    """
    try:
        with open(arquivo, "w") as f:
            f.write(conteudo)
        console.success(f"conteúdo escrito em [bold]{arquivo}[/bold] com sucesso")
    except PermissionError:
        raise console.error("você não possui permissão para escrever no arquivo")
    except FileNotFoundError:
        raise console.error(f"caminho não existente {dirname(arquivo)}")
    except Exception as exc:
        raise console.error(f"não foi possível escrever no arquivo: {exc!s}")


@app.command("ler")
def ler(
    arquivo: Annotated[Path, typer.Argument()],
):
    """
    Lê e exibe o conteúdo de um arquivo no caminho especificado
    """
    try:
        with open(arquivo, "r") as f:
            print(f"[bold] {arquivo}:[/bold]")
            print(f.read())
    except PermissionError:
        raise console.error("você não possui permissão para ler o arquivo")
    except FileNotFoundError:
        raise console.error(f"arquivo não encontrado: {arquivo}")
    except IsADirectoryError:
        raise console.error(f"{arquivo} é um diretório, não um arquivo")
    except Exception as exc:
        raise console.error(f"não foi possível ler o arquivo: {exc!s}")


@app.command("renomear")
def renomear(
    arquivo: Annotated[Path, typer.Argument()],
    novo_nome: Annotated[str, typer.Argument()],
):
    """
    Renomeia um arquivo existente no caminho especificado
    """
    try:
        directory = dirname(arquivo)
        novo_caminho = Path(directory, novo_nome)
        os.rename(arquivo, novo_caminho)
        console.success(f"{arquivo} foi renomeado para {novo_nome} com sucesso")
    except FileNotFoundError:
        raise console.error(f"arquivo não encontrado: {arquivo}")
    except PermissionError:
        raise console.error("você não possui permissão para renomear o arquivo")
    except Exception as exc:
        raise console.error(f"não foi possível renomear o arquivo: {exc!s}")


@app.command("remover")
def remover(
    arquivo: Annotated[Path, typer.Argument()],
):
    """
    Remove o arquivo no caminho especificado
    """
    try:
        os.remove(arquivo)
        console.success(f"{arquivo} foi excluído com sucesso")
    except PermissionError:
        raise console.error("você não possui permissão para remover o arquivo")
    except FileNotFoundError:
        raise console.error(f"arquivo não existente {arquivo}")
    except Exception as exc:
        raise console.error(f"não foi possível remover o arquivo: {exc!s}")
