import click

@click.command()
@click.argument('key')
def remove(key):
    click.echo(f"remove key={key}")
