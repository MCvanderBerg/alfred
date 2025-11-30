import click
import json
from importlib.resources import files

@click.command()
@click.argument('key')
def get(key):
    with (files("alfred_cli.kvm") / "data.json").open() as f:
        data = json.load(f)

    try:
        value = data[key]
    except KeyError:
            click.echo(f"no value associated to this key {key}")
            raise SystemExit(1)

    click.echo(value)


