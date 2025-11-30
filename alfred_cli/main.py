import os
from pathlib import Path

import click

from alfred_cli.dam import dam_group
from alfred_cli.kvm import kvm_group


@click.group()
def cli():
    """Alfred: CLI toolchain helper."""


@cli.command()
def init():
    """
    One-time shell setup for Alfred.

    This appends the necessary snippet to your ~/.zshrc so that
    DAM aliases and the dam() helper function are available in
    every new shell.
    """
    zshrc_path = Path(os.path.expanduser("~/.zshrc"))
    # Full shell integration snippet.
    # NOTE: we avoid hardcoding the project path and use the installed
    # CLI instead of sourcing a local script.
    snippet = """# Alfred CLI shell integration
eval "$(alfred dam env)"

dam() {
  # Call the real dam CLI
  command dam "$@"
  local exit_status=$?

  # After successful operations, manage aliases
  if [[ $exit_status -eq 0 ]]; then
    if [[ "$1" == "add" ]]; then
      # Reload aliases to include the new key
      eval "$(alfred dam env)"
    elif [[ "$1" == "remove" && -n "$2" ]]; then
      # Remove the alias/env corresponding to the removed key, if it exists
      unalias "__$2" 2>/dev/null
      unset "$2" 2>/dev/null
    fi
  fi

  return $exit_status
}
"""

    existing = zshrc_path.read_text() if zshrc_path.exists() else ""

    if snippet in existing:
        click.echo("Alfred shell integration is already present in ~/.zshrc")
        return

    lines = []
    if existing:
        lines.append(existing.rstrip("\n"))

    lines.append("")
    lines.append(snippet.rstrip("\n"))
    lines.append("")

    zshrc_path.write_text("\n".join(lines))

    click.echo('Added Alfred shell integration to ~/.zshrc.')
    click.echo('Restart your terminal or run: source ~/.zshrc')


cli.add_command(kvm_group, name="kvm")
cli.add_command(dam_group, name="dam")


if __name__ == "__main__":
    cli()
