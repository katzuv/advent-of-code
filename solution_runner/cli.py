import click

from solution_runner.consts import CliConstants


@click.group(context_settings=CliConstants.CONTEXT)
def cli() -> click.Group:
    """
    Main CLI holding all Advent of Code related commands.

    For more information about Advent of Code, see https://adventofcode.com.
    """


def main():
    """Add subcommands to the solution runner CLI and run it."""
    cli()


if __name__ == '__main__':
    main()
