import click
from pathlib import Path

@click.command()
@click.option('--name', '-n', required=True, type = str, help="The name of the person")
@click.option('--age', '-a', required=True, type=int, help="The age of the person")
def cli(name, age):
    click.echo(f"Hello {name}, you are {age} years old")

if __name__ == "__main__":
    cli()