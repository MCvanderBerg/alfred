import click
import json
from pathlib import Path

@click.command()
@click.argument('key')
def get(key):
    data_path = Path(__file__).with_name("data.json")
    with data_path.open() as f:
        data = json.load(f)

    try:
        value = data[key]
    except KeyError:
            click.echo(f"no value associated to this key {key}")
            raise SystemExit(1)

    click.echo(value)


