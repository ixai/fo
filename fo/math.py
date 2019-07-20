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
        self, left_operand: float, operator: str, right_operand: float
    ) -> None:
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

    def operate(self) -> float:
        """Perform the operation described by the Operation instance"""
        return self._operation_map[self.operator](self.left_operand, self.right_operand)
