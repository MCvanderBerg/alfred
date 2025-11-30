import click
import json
import os
from pathlib import Path

@click.command()
@click.option("--key", "-k", required=False, help="Name to use as the alias key")
@click.option("--value", "-v", required=False, help="Path to associate with the key")
def add(key, value):
    """
    Add a key/value mapping for dam.

    Examples:
      dam add                -> key = folder name, value = $PWD
      dam add -k KEY         -> key = KEY,         value = $PWD
      dam add -k KEY -v VAL  -> key = KEY,         value = VAL
    """
    # Always use the data.json that lives next to this file
    data_path = Path(__file__).with_name("data.json")

    cwd = os.getcwd()
    if key is None:
        key = os.path.basename(cwd.rstrip(os.sep)) or cwd
    if value is None:
        value = cwd

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
