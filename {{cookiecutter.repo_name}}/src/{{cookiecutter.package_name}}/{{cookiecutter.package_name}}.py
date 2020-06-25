"""This is a Docstring"""
import re
from typing import Tuple, List
import random
import typer

app = typer.Typer()


try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version("{{cookiecutter.package_name}}")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


def version_callback(value: bool):
    """ Check that we have a version response for this application. """
    if value:
        typer.echo(f"Version: {__version__}")
        raise typer.Exit()


def roll(num_dice: int = 1, sides: int = 20) -> Tuple[List[int], int]:
    """Docstring goes here"""
    rolls = sorted(
        [random.choice(range(1, sides + 1)) for _ in range(num_dice)], reverse=True
    )
    return (rolls, sum(rolls))


@app.command("roll-num")
def roll_num(
    num_dice: int = typer.Option(  # noqa: B008
        1, "-n", "--num-dice", help="number of dice to roll", show_default=True, min=1
    ),
    sides: int = typer.Option(  # noqa: B008
        20, "-d", "--sides", help="number-sided dice to roll", show_default=True, min=1
    ),
    rolls: bool = typer.Option(  # noqa: B008
        False, help="set to display individual rolls", show_default=True
    ),
):
    """Rolls the dice from numeric inputs.

    We supply the number and side-count of dice to roll with option arguments.
    """
    rolls_list, total = roll(num_dice=num_dice, sides=sides)

    typer.echo(f"rolling {num_dice}D{sides}!\n")
    typer.echo(f"your roll: {total}\n")
    if rolls:
        typer.echo(f"made up of {rolls_list}\n")


def parse_dice_string(dice_string: str) -> Tuple[int, int]:
    """Extract digits from dice-roll strings like "2D6" with regex witchcraft"""
    hit = re.search(r"(\d*)[dD](\d+)", dice_string)
    if not hit:
        raise ValueError("bad string")

    count, sides = hit.groups()
    count_int = int(count or 1)  # regex hits on "" for 1st digit, munge to 1
    sides_int = int(sides)
    return (count_int, sides_int)


def roll_from_string(dice_string: str) -> Tuple[List[int], int, str]:
    """Docsting goes here."""
    count, sides = parse_dice_string(dice_string)
    rolls, total = roll(num_dice=count, sides=sides)
    return (rolls, total, f"{count}D{sides}")


@app.command("hello")
def hello_world():
    """our first CLI with typer!
    """
    typer.echo("Opening blog post...")
    typer.launch(
        "https://pluralsight.com/tech-blog/python-cli-utilities-with-poetry-and-typer"
    )


@app.command("roll-str")
def roll_string(dice_str: str):
    """Rolls the dice from a formatted string.

    We supply a formatted string DICE_STR describing the roll, e.g. '2D6'
    for two six-sided dice.
    """
    try:
        rolls_list, total, formatted_roll = roll_from_string(dice_str)
    except ValueError:
        typer.echo(f"invalid roll string: {dice_str}")
        raise typer.Exit(code=1)

    typer.echo(f"rolling {formatted_roll}!\n")
    typer.echo(f"your roll: {total}\n")

@app.command()
def main(
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    """ DocString goes here. """

    # do stuff here.
    return

