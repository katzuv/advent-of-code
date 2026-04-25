import os

import click_completion
import click_completion.core
import rich_click as click


# 1. Custom matching logic
def custom_startswith(string, incomplete):
    """A custom completion matching that supports case insensitive matching"""
    if os.environ.get("_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE"):
        string = string.lower()
        incomplete = incomplete.lower()
    return string.startswith(incomplete)


# 2. Initialize the click_completion engine
click_completion.core.startswith = custom_startswith
click_completion.init()

# 3. Dynamic help text
cmd_help = """Shell completion commands.

Available shell types:

\b
  {}

Default type: auto
""".format(
    "\n  ".join(
        f"{k:<12} {click_completion.core.shells[k]}"
        for k in sorted(click_completion.core.shells.keys())
    )
)


# 4. Create the group that will hold the show/install commands
@click.group(name="completion", help=cmd_help)
def completion_group():
    pass


@completion_group.command()
@click.option(
    "-i", "--case-insensitive/--no-case-insensitive", help="Case insensitive completion"
)
@click.argument(
    "shell",
    required=False,
    type=click_completion.DocumentedChoice(click_completion.core.shells),
)
def show(shell, case_insensitive):
    """Show the completion code"""
    extra_env = (
        {"_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE": "ON"}
        if case_insensitive
        else {}
    )
    click.echo(click_completion.core.get_code(shell, extra_env=extra_env))


@completion_group.command()
@click.option(
    "--append/--overwrite", help="Append the completion code to the file", default=None
)
@click.option(
    "-i",
    "--case-insensitive/--no-case-insensitive",
    default=True,
    help="Case insensitive completion",
)
@click.argument(
    "shell",
    required=False,
    type=click_completion.DocumentedChoice(click_completion.core.shells),
)
@click.argument("path", required=False)
def install(append, case_insensitive, shell, path):
    """Install the completion script to your shell profile"""
    extra_env = (
        {"_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE": "ON"}
        if case_insensitive
        else {}
    )
    shell, path = click_completion.core.install(
        shell=shell, path=path, append=append, extra_env=extra_env
    )
    click.echo(f"{shell} completion installed in {path}")
