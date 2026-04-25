import os
import shutil
import subprocess
from pathlib import Path

import rich_click as click
from click.parser import split_arg_string
from click.shell_completion import CompletionItem, ShellComplete, add_completion_class

# ==============================================================================
# VENDORED SCRIPT: click-pwsh
# Copyright 2022 Yu-Kai Lin. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Source: https://github.com/StephLin/click-pwsh
# ==============================================================================

_SOURCE_PWSH = """\
Register-ArgumentCompleter -Native -CommandName %(prog_name)s -ScriptBlock {
    param($wordToComplete, $commandAst, $cursorPosition)
        $env:COMP_WORDS = $commandAst
        $env:COMP_WORDS = $env:COMP_WORDS.replace('\\', '/')
        $incompleteCommand = $commandAst.ToString()

        $myCursorPosition = $cursorPosition
        if ($myCursorPosition -gt $incompleteCommand.Length) { $myCursorPosition = \
$incompleteCommand.Length }
        $env:COMP_CWORD = @($incompleteCommand.substring(0, \
$myCursorPosition).Split(" ") | Where-Object { $_ -ne "" }).Length
        if ( $wordToComplete.Length -gt 0) { $env:COMP_CWORD -= 1 }

        $env:%(complete_var)s = "pwsh_complete"

        %(prog_name)s | ForEach-Object {
            $type, $value, $help = $_.Split(",", 3)
            if ( ($type -eq "plain") -and ![string]::IsNullOrEmpty($value) ) {
                [System.Management.Automation.CompletionResult]::new($value, $value, \
"ParameterValue", $value)
            } elseif ( ($type -eq "file") -or ($type -eq "dir") ) {
                if ([string]::IsNullOrEmpty($wordToComplete)) {
                    $dir = "./"
                } else {
                    $dir = $wordToComplete.replace('\\', '/')
                }
                if ( (Test-Path -Path $dir) -and ((Get-Item $dir) -is \
[System.IO.DirectoryInfo]) ) {
                    [System.Management.Automation.CompletionResult]::new($dir, $dir, \
"ParameterValue", $dir)
                }
                Get-ChildItem -Path $dir | Resolve-Path -Relative | ForEach-Object {
                    $path = $_.ToString().replace('\\', \
'/').replace('Microsoft.PowerShell.Core/FileSystem::', '')
                    $isDir = $false
                    if ((Get-Item $path) -is [System.IO.DirectoryInfo]) {
                        $path = $path + "/"
                        $isDir = $true
                    }
                    if ( ($type -eq "file") -or ( ($type -eq "dir") -and $isDir ) ) {
                        [System.Management.Automation.CompletionResult]::new($path, \
$path, "ParameterValue", $path)
                    }
                }
            }
        }

        $env:COMP_WORDS = $null | Out-Null
        $env:COMP_CWORD = $null | Out-Null
        $env:%(complete_var)s = $null | Out-Null
}
"""


class PwshComplete(ShellComplete):
    """Shell completion for PowerShell 7."""

    name = "pwsh"
    source_template = _SOURCE_PWSH

    def get_completion_args(self) -> tuple[list[str], str]:
        cwords = split_arg_string(os.environ["COMP_WORDS"])
        cword = int(os.environ["COMP_CWORD"])
        args = cwords[1:cword]
        try:
            incomplete = cwords[cword]
        except IndexError:
            incomplete = ""
        return args, incomplete

    def format_completion(self, item: CompletionItem) -> str:
        return f"{item.type},{item.value},{item.help if item.help else '_'}"


# Register the vendored completion class with Click
add_completion_class(PwshComplete)

# ==============================================================================
# END VENDORED SCRIPT
# ==============================================================================


@click.group(name="completion")
def completion_group():
    """Shell completion utilities."""
    pass


@completion_group.command()
def install():
    """Install PowerShell 7 completion directly to your $PROFILE."""
    from .cli import cli  # Lazy import to avoid circular dependency

    # 1. Initialize the custom PwshComplete class we just registered
    comp = PwshComplete(
        cli=cli, ctx_args={}, prog_name="aoc", complete_var="_AOC_COMPLETE"
    )
    script = comp.source()

    # 2. Use modern pwsh if available, fallback to powershell
    shell_exe = "pwsh" if shutil.which("pwsh") else "powershell"

    # 3. Locate the profile via a subprocess call to bypass environment quirks
    try:
        profile_path = (
            subprocess.check_output(
                [shell_exe, "-NoProfile", "-Command", "Write-Output $PROFILE"]
            )
            .decode()
            .strip()
        )
    except subprocess.CalledProcessError:
        click.secho("Failed to locate PowerShell profile.", fg="red")
        raise click.Abort from None

    # 4. Write the modern script to the profile safely
    profile = Path(profile_path)
    profile.parent.mkdir(parents=True, exist_ok=True)

    with open(profile, "a", encoding="utf-8") as f:
        f.write("\n\n# --- AOC Autocomplete (PWSH 7+) ---\n")
        f.write(script)
        f.write("\n# ----------------------------------\n")

    click.secho(
        f"Successfully installed modern pwsh completion to: {profile}", fg="green"
    )
    click.secho("Restart your terminal and type 'aoc s<Tab>' to test it!", fg="cyan")
