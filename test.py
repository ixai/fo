import click
from click.testing import CliRunner
from pytest import fixture

from fo import OperationParam, fraction_operation


@fixture
def runner() -> CliRunner:
    return CliRunner()


def test_optional_operation_prefix(runner: CliRunner) -> None:
    @click.command()
    @click.argument("operation", type=OperationParam())
    def cli(operation: str) -> None:
        pass

    operations = ("? 1 + 1", "1 + 1")
    for operation in operations:
        result = runner.invoke(cli, [operation])
        assert result.exit_code == 0

    result = runner.invoke(cli, ["¿ 1 + 1"])
    assert result.exit_code == 2


def test_malformed_operation(runner: CliRunner) -> None:
    @click.command()
    @click.argument("operation", type=OperationParam())
    def cli(operation: str) -> None:
        pass

    malformed_operations = (
        "? 1 + ",
        "? 1 + 1 + 3",
        "? 1 + 1/",
        "? 1 x 1",
        "? 1_1 + 1",
        "? 1",
        "? + 1/3",
        "? 1/0 + 1",
    )
    for operation in malformed_operations:
        result = runner.invoke(cli, operation)
        assert result.exit_code == 2


def test_integer_operations(runner: CliRunner) -> None:
    operation_map = {"+": "6", "-": "0", "*": "9", "/": "1"}

    for operator, result in operation_map.items():
        _result = runner.invoke(fraction_operation, [f"? 3 {operator} 3"])
        assert _result.exit_code == 0
        assert _result.output == f"{result}\n"
