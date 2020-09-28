"""This is a docstring to help you undersyand your tests later."""
from typer.testing import CliRunner
from {{cookiecutter.package_name}}.{{cookiecutter.package_name}} import roll_num
import re

runner = CliRunner()


def test_version():
    """Doc string goes here"""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "Version" in result.stdout


def test_roll_num(capsys):
    """Doc string goes here"""
    roller = roll_num(num_dice=1, sides=20)  # noqa: F841
    stdout = capsys.readouterr().out

    regex = re.compile(r"rolling (\d+D\d+)!\n\nyour roll: (\d+)")
    roll_str, total = re.search(regex, stdout).groups()
    assert roll_str == "1D20"
    assert int(total) in range(1, 21)


def test_parse_dice_string_good_input():
    """Check that we get expected output for "2D6"
    """
    result = parse_dice_string("2D6")

    assert result[0] == int(2)
    assert result[1] == int(6)


def test_parse_dice_string_unknown_input():
    """Check that we get expected output error for input "ZZZZ"
    that does not match the expected argument format
    """
    with pytest.raises(Exception) as e_info:
        result = parse_dice_string("ZZZZ")  # noqa: F841
    assert e_info.value.args[0] == "bad string"
