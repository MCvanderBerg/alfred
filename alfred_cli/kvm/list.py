import click
import json
from importlib.resources import files


@click.command()
def list():
    """List all stored key/value pairs.

    Falls back to an empty mapping if the backing store doesn't exist yet
    or is unreadable.
    """
    data_path = files("alfred_cli.kvm") / "data.json"

    try:
        with data_path.open() as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if not data:
        click.echo("no kvm entries yet")
        return

    # Print one key/value per line
    for key, value in data.items():
        click.echo(f"{key}: {value}")
