import rich_click as click

import commands

CONTEXT = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT)
def cli() -> click.Group:
    """
    Make your Advent of Code journey easier.

    For more information about Advent of Code, see https://adventofcode.com.
    """


if __name__ == "__main__":
    cli.add_command(commands.setup)
    cli.add_command(commands.config)
    cli.add_command(commands.submit)
    cli()
