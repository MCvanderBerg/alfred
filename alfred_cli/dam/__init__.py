import click

from .add import add
from .env import env
from .get import get
from .list import list
from .remove import remove


@click.group()
def dam_group():
    """Commands for managing and loading directory aliases (DAM)."""


dam_group.add_command(add)
dam_group.add_command(remove)
dam_group.add_command(list)
dam_group.add_command(get)
dam_group.add_command(env)
