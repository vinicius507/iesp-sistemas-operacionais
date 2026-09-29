import os
from pathlib import Path
from typing import Annotated

import typer
from rich import print

from sistemas_operacionais import console

app = typer.Typer(help="Comandos para criar e listar diretórios")


@app.command("criar")
def criar(caminho: Annotated[Path, typer.Argument()]):
    """
    Cria um diretório no caminho especificado
    """
    try:
        os.makedirs(caminho, exist_ok=True)
        console.success(f"diretório [bold]{caminho}[/bold] criado com sucesso")
    except PermissionError:
        raise console.error("você não possui permissão para criar o diretório")
    except Exception as exc:
        raise console.error(f"não foi possível criar o diretório: {exc!s}")


@app.command("listar")
def listar(caminho: Annotated[Path, typer.Argument(default_factory=lambda: Path("."))]):
    """
    Lista o conteúdo de um diretório
    """
    try:
        entradas = sorted(os.listdir(caminho))

        print(f"[bold]📂 {caminho}[/bold]")
        for entrada in entradas:
            completo = Path(caminho, entrada)
            if completo.is_dir():
                print(f"[bold blue]📁 {entrada}/[/bold blue]")
                continue
            print(f"📄 {entrada}")
    except PermissionError:
        raise console.error("você não possui permissão para listar o diretório")
    except FileNotFoundError:
        raise console.error(f"diretório não encontrado: {caminho}")
    except NotADirectoryError:
        raise console.error(f"{caminho} não é um diretório")
    except Exception as exc:
        raise console.error(f"não foi possível listar o diretório: {exc!s}")
