import typer
from rich.console import Console

console = Console(stderr=True)


def success(msg: str) -> None:
    console.print("[bold green]✓[/bold green]", msg, sep=" ")


def error(msg: str, *, exit_code: int = 1) -> typer.Exit:
    console.print("[bold][red]✗[/red] Erro:[/bold]", msg, sep=" ")
    return typer.Exit(exit_code)
