import os

import typer

from sistemas_operacionais import console

app = typer.Typer(help="Comandos para gerenciamento de processos")


@app.command("pid")
def pid():
    """
    Imprime o PID do processo atual
    """
    console.success(f"PID do processo atual: [bold]{os.getpid()}[/bold]")
