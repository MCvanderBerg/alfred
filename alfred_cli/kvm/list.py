import click
import json
from importlib.resources import files

@click.command()
def list():
    with (files("alfred_cli.kvm") / "data.json").open() as f:
        data = json.load(f)
        click.echo(data)
