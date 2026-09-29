import typer

from sistemas_operacionais.comandos import arquivo, diretorio, processo

app = typer.Typer(
    help="Aplicação em Python construida para disciplina de sistemas operacionais"
)
app.add_typer(arquivo.app, name="arquivo")
app.add_typer(diretorio.app, name="diretorio")
app.add_typer(processo.app, name="processo")


def main():
    app()


if __name__ == "__main__":
    main()
