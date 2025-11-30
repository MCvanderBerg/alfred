import click


from .add import add
from .remove import remove
from .list import list
from .get import get

@click.group()
def kvm_group():
    pass

kvm_group.add_command(add)
kvm_group.add_command(remove)
kvm_group.add_command(list)
kvm_group.add_command(get)
