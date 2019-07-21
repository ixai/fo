def gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of two numbers"""
    while b != 0:
        a, b = b, a % b

    return a


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: "Fraction") -> "Fraction":
        numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator
        return Fraction(numerator=numerator, denominator=denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator
        return Fraction(numerator=numerator, denominator=denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator=numerator, denominator=denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        numerator = self.numerator * other.denominator
        denominator = other.numerator * self.denominator
        return Fraction(numerator=numerator, denominator=denominator)

    def __str__(self) -> str:
        sign_prefix = "-" if (self.numerator / self.denominator) < 0 else ""
        numerator = abs(self.numerator)
        denominator = abs(self.denominator)
        _gcd = gcd(numerator, denominator)
        numerator = numerator // _gcd
        denominator = denominator // _gcd
        whole = numerator // denominator
        numerator = numerator % denominator

        if not whole and not numerator:
            return "0"
        elif whole and not numerator:
            return f"{sign_prefix}{whole}"
        elif numerator and not whole:
            return f"{sign_prefix}{numerator}/{denominator}"
        else:
            return f"{sign_prefix}{whole}_{numerator}/{denominator}"


class Operation:
    """Represents an arithmetic operation composed of two operands and one operator"""

    # Maps string operators to a function performing the relevant operation
    _operation_map = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    def __init__(
        self, left_operand: Fraction, operator: str, right_operand: Fraction
    ) -> None:
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

    def operate(self) -> Fraction:
        """Perform the operation described by the Operation instance"""
        return self._operation_map[self.operator](self.left_operand, self.right_operand)


__all__ = ["Fraction", "Operation"]
