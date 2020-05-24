"""This is a docstring to help you undersyand your tests later."""
from {{cookiecutter.package_name}}.{{cookiecutter.package_name}} import roll_num
import re


def test_roll_num(capsys):
    """Doc string goes here"""
    roller = roll_num(num_dice=1, sides=20)  # noqa: F841
    stdout = capsys.readouterr().out

    regex = re.compile(r"rolling (\d+D\d+)!\n\nyour roll: (\d+)")
    roll_str, total = re.search(regex, stdout).groups()
    assert roll_str == "1D20"
    assert int(total) in range(1, 21)
