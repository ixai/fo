from typing import Callable, Dict

import click
from click.testing import CliRunner
from pytest import fixture

from fo import OperationParam, fraction_operation


@fixture
def runner() -> CliRunner:
    return CliRunner()


@fixture
def assert_all_operators(runner: CliRunner) -> Callable[..., None]:
    def _assert_all_operators(
        left_operand: str, right_operand: str, operation_map: Dict[str, str]
    ) -> None:
        for operator, result in operation_map.items():
            _result = runner.invoke(
                fraction_operation, [f"? {left_operand} {operator} {right_operand}"]
            )
            assert _result.exit_code == 0
            assert _result.output == f"= {result}\n"

    return _assert_all_operators


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


def test_integer_operations(assert_all_operators: Callable[..., None]) -> None:
    operation_map = {"+": "6", "-": "0", "*": "9", "/": "1"}
    assert_all_operators("3", "3", operation_map)


def test_fraction_operations(assert_all_operators: Callable[..., None]) -> None:
    operation_map = {"+": "2/3", "-": "0", "*": "1/9", "/": "1"}
    assert_all_operators("1/3", "1/3", operation_map)


def test_mixed_fraction_operations(assert_all_operators: Callable[..., None]) -> None:
    operation_map = {"+": "6_2/3", "-": "0", "*": "11_1/9", "/": "1"}
    assert_all_operators("3_1/3", "3_1/3", operation_map)


def test_negative_operands(assert_all_operators: Callable[..., None]) -> None:
    operation_map = {"+": "0", "-": "-6_2/3", "*": "-11_1/9", "/": "-1"}
    assert_all_operators("-3_1/3", "3_1/3", operation_map)


def test_negative_results(runner: CliRunner) -> None:
    operation_map = {"1": "-1", "1/3": "-1/3", "3_1/3": "-3_1/3"}

    for operand, result in operation_map.items():
        _result = runner.invoke(fraction_operation, [f"? 0 - {operand}"])
        assert _result.exit_code == 0
        assert _result.output == f"= {result}\n"

def test_false():
    assert False

