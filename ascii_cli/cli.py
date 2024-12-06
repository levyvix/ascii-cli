from typing import Annotated

import pyfiglet
import typer

app = typer.Typer()


@app.command()
def print_text(text: Annotated[str, typer.Argument()], font: Annotated[str, typer.Option()] = "slant"):
    typer.echo(f"Printing: {text}")
    ascii_art = pyfiglet.figlet_format(text, font=font)
    typer.echo(ascii_art)


if __name__ == "__main__":
    app()
