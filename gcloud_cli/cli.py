# -*- coding: utf-8 -*-

"""Console script for gcloud_cli."""

import click
from .pubsub import commands as pubsub_commands
from . import __version__


CONTEXT_SETTINGS = dict(
    obj={},
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def main(ctx, debug):
    """Console script for gcloud_cli."""
    pass


@main.command()
def version():
    """Display the current version."""
    click.echo(__version__)

main.add_command(pubsub_commands.pubsub)


if __name__ == "__main__":
    main()
