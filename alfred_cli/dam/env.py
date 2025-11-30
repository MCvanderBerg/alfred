import json
from importlib.resources import files

import click


@click.command()
def env():
    """
    Print shell commands to load DAM aliases and exports.

    Usage in your shell (e.g. in ~/.zshrc):

        eval "$(alfred dam env)"
    """
    data_path = files("alfred_cli.dam") / "data.json"

    try:
        with data_path.open() as f:
            data = json.load(f)
    except FileNotFoundError:
        # If there is no data file yet, just do nothing.
        return

    for key, path in data.items():
        if not key:
            continue

        # Create an alias that cds into the stored path
        click.echo(f'alias "__{key}"="cd {path}"')
        click.echo(f'export {key}="{path}"')


