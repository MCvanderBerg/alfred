import click
import json
from pathlib import Path


@click.command()
@click.argument('key')
def remove(key):
    """Remove a key from dam's data.json."""
    data_path = Path(__file__).with_name("data.json")

    # Load existing data (if any)
    try:
        with data_path.open() as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}

    if key not in data:
        raise SystemExit(1)

    # Remove the key and write back
    del data[key]

    with data_path.open("w") as f:
        json.dump(data, f, indent=2)
