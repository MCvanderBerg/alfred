import click
import json
from importlib.resources import files

@click.command()
@click.argument('key')
@click.argument('value')
def add(key, value):
    data_path = files("alfred_cli.kvm") / "data.json"

    # Read existing data
    try:
        with data_path.open() as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}

    data[key] = value

    with data_path.open("w") as f:
        json.dump(data, f, indent=2)

