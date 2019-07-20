import click

from .math import Operation
from .types import OperationParam


@click.command()
@click.argument("operation", type=OperationParam())
def fraction_operation(operation: Operation) -> None:
    """Perform fractions operations"""
    result = operation.operate()
    click.echo(f"{result:.0f}")
