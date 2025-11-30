import click
import json
from pathlib import Path


@click.command()
def list():
    """List all dam entries, one per line."""
    data_path = Path(__file__).with_name("data.json")
    with data_path.open() as f:
        data = json.load(f)

    # Print one key/value per line
    for key, value in data.items():
        click.echo(f"{key}: {value}")
