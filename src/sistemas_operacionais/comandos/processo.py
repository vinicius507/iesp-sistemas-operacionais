import os
import subprocess
from typing import Annotated

import typer
from rich import print

from sistemas_operacionais import console

app = typer.Typer(help="Comandos para gerenciamento de processos")


@app.command("pid")
def pid():
    """
    Imprime o PID do processo atual
    """
    console.success(f"PID do processo atual: [bold]{os.getpid()}[/bold]")


@app.command(
    "executar",
    context_settings={
        "allow_extra_args": True,
        "allow_interspersed_args": False,
    },
)
def executar(ctx: typer.Context, comando: Annotated[str, typer.Argument()]):
    """
    Cria um processo filho, exibe seu PID e aguarda sua finalização
    """
    try:
        print(
            f"[bold]$[/bold] {comando} {' '.join(f'"{arg}"' if ' ' in arg else arg for arg in ctx.args)}"
        )
        args = [comando, *ctx.args]
        processo = subprocess.Popen(args)
        console.success(f"processo criado com PID [bold]{processo.pid}[/bold]")

        returncode = processo.wait()

        if returncode == 0:
            console.success(
                f"processo [bold]{processo.pid}[/bold] finalizado com código [bold]{returncode}[/bold]"
            )
            return
        raise console.error(
            f"processo [bold]{processo.pid}[/bold] finalizado com código [bold]{returncode}[/bold]"
        )
    except FileNotFoundError:
        raise console.error(f"comando não encontrado: {comando}")
    except Exception as exc:
        if isinstance(exc, typer.Exit):
            raise
        raise console.error(f"não foi possível executar o comando: {exc!s}")
