import re
from typing import Optional

import click

from .math import Operation

INTEGER_RE = re.compile(r"^-?(?P<whole>\d+)$")
FRACTION_RE = re.compile(r"^-?(?P<numerator>\d+)/(?P<denominator>\d+)$")
MIXED_FRACTION_RE = re.compile(
    r"^-?(?P<whole>\d+)_(?P<numerator>\d+)/(?P<denominator>\d+)$"
)
VALID_OPERATORS = ("+", "-", "*", "/")


class InvalidOperandError(Exception):
    def __init__(self, operand: str) -> None:
        super().__init__(f"Invalid operand: {operand}.")


class InvalidOperatorError(Exception):
    def __init__(self, operator: str) -> None:
        super().__init__(f"Invalid operator: {operator}.")


class OperationParam(click.ParamType):
    name = "operation_parameter"

    def convert(
        self, value: str, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> Operation:
        """Return an instance of an Operation object representing the arithmetic operation described by the `value` argument"""
        parts = value.split()
        if parts[0] == "?":
            parts = parts[1:]

        if len(parts) != 3:
            self.fail(f"{value} is not a valid operation", param, ctx)

        try:
            left_operand = self._parse_operand(parts[0])
            operator = self._parse_operator(parts[1])
            right_operand = self._parse_operand(parts[2])
        except (InvalidOperandError, InvalidOperatorError) as e:
            self.fail(f"{e}", param, ctx)

        return Operation(left_operand, operator, right_operand)

    def _parse_operand(self, operand: str) -> float:
        for regex in (INTEGER_RE, FRACTION_RE, MIXED_FRACTION_RE):
            match = regex.match(operand)
            if match:
                break

        if not match:
            raise InvalidOperandError(operand)

        denominator = int(match.groupdict().get("denominator", 1))
        if denominator == 0:
            raise InvalidOperandError(operand)

        whole = int(match.groupdict().get("whole", 0))
        numerator = whole * denominator + int(match.groupdict().get("numerator", 0))
        if operand.startswith("-"):
            numerator *= -1

        return numerator // denominator

    def _parse_operator(self, operator: str) -> str:
        if operator not in VALID_OPERATORS:
            raise InvalidOperatorError(operator)

        return operator
