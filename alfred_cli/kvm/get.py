import click
import json
from importlib.resources import files


@click.command()
@click.argument("key")
def get(key):
    """Get a value by key from the backing store."""
    data_path = files("alfred_cli.kvm") / "data.json"

    try:
        with data_path.open() as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        click.echo("no data store found yet")
        raise SystemExit(1)

    try:
        value = data[key]
    except KeyError:
        click.echo(f"no value associated to this key {key}")
        raise SystemExit(1)

    click.echo(value)
