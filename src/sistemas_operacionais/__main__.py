import typer

from sistemas_operacionais.comandos import arquivo, diretorio

app = typer.Typer(
    help="Aplicação em Python construida para disciplina de sistemas operacionais"
)
app.add_typer(arquivo.app, name="arquivo")
app.add_typer(diretorio.app, name="diretorio")


def main():
    app()


if __name__ == "__main__":
    main()
