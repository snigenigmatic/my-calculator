"""
Calculator Module - Basic arithmetic operations with history tracking
Students will extend this with more functions
"""
from datetime import datetime
from typing import Any


class CalculatorHistory:
    """Manages calculation history for the calculator."""

    def __init__(self):
        """Initialize empty history."""
        self._history: list[dict[str, Any]] = []

    def add_entry(
        self,
        operation: str,
        operands: list[float],
        result: float,
        timestamp: datetime | None = None,
    ) -> None:
        """Add a calculation entry to history.

        Args:
            operation: The operation performed (e.g., 'add', 'multiply')
            operands: List of operands used in the calculation
            result: The result of the calculation
            timestamp: When the calculation was performed (defaults to now)
        """
        if timestamp is None:
            timestamp = datetime.now()

        entry = {
            'operation': operation,
            'operands': operands.copy(),
            'result': result,
            'timestamp': timestamp,
            'expression': self._format_expression(operation, operands, result)
        }
        self._history.append(entry)

    def _format_expression(
        self, operation: str, operands: list[float], result: float
    ) -> str:
        """Format the calculation as a readable expression."""
        # Use a dictionary to reduce the number of return statements
        formatters = {
            "add": lambda ops, res: f"{ops[0]} + {ops[1]} = {res}",
            "subtract": lambda ops, res: f"{ops[0]} - {ops[1]} = {res}",
            "multiply": lambda ops, res: f"{ops[0]} x {ops[1]} = {res}",
            "divide": lambda ops, res: f"{ops[0]} ÷ {ops[1]} = {res}",
            "power": lambda ops, res: f"{ops[0]} ^ {ops[1]} = {res}",
            "sqrt": lambda ops, res: f"√{ops[0]} = {res}",
        }

        if operation in formatters:
            return formatters[operation](operands, result)

        return f"{operation}({', '.join(map(str, operands))}) = {result}"

    def get_history(self, limit: int | None = None) -> list[dict[str, Any]]:
        """Get calculation history.

        Args:
            limit: Maximum number of entries to return (newest first)

        Returns:
            List of history entries
        """
        history = self._history.copy()
        history.reverse()  # Most recent first
        if limit is not None:
            history = history[:limit]
        return history

    def get_last_result(self) -> float | None:
        """Get the result of the last calculation."""
        if not self._history:
            return None
        return self._history[-1]['result']

    def clear_history(self) -> int:
        """Clear all history entries.

        Returns:
            Number of entries that were cleared
        """
        count = len(self._history)
        self._history.clear()
        return count

    def get_history_count(self) -> int:
        """Get the total number of calculations in history."""
        return len(self._history)


# Global history instance
_calculator_history = CalculatorHistory()


def add(a, b):
    """Add two numbers together"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    result = a + b
    _calculator_history.add_entry("add", [a, b], result)
    return result


def subtract(a, b):
    """Subtract b from a"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    result = a - b
    _calculator_history.add_entry("subtract", [a, b], result)
    return result


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    print(f"Multiplying {a} x {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    _calculator_history.add_entry("multiply", [a, b], result)
    return result


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")

    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    _calculator_history.add_entry("divide", [a, b], result)
    return result


# TODO: Students will add multiply, divide, power, sqrt functions


def power(a, b):
    """Raise a to the power of b"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    # Check for potentially problematic cases that would result in very large numbers
    # Rough heuristic: if b is very large, it's likely to cause overflow
    if isinstance(a, int) and isinstance(b, int) and b > 0 and b > 10000:
        raise OverflowError("Result too large to represent")

    try:
        result = a**b
        if result == float("inf") or result == float("-inf"):
            raise OverflowError("Result too large to represent")

        # Try to convert to string to detect if it's too large for representation
        try:
            str(result)
        except ValueError as str_e:
            if "Exceeds the limit" in str(str_e) and "integer string conversion" in str(
                str_e
            ):
                raise OverflowError("Result too large to represent") from None
    except OverflowError:
        raise OverflowError("Result too large to represent") from None
    else:
        _calculator_history.add_entry("power", [a, b], result)
        return result


def sqrt(a):
    """Return the square root of a"""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    result = a**0.5
    _calculator_history.add_entry("sqrt", [a], result)
    return result


# History management functions


def get_calculation_history(limit: int | None = None) -> list[dict[str, Any]]:
    """Get the calculation history.

    Args:
        limit: Maximum number of entries to return (newest first)

    Returns:
        List of history entries with calculation details
    """
    return _calculator_history.get_history(limit)


def print_history(limit: int | None = None) -> None:
    """Print the calculation history in a readable format.

    Args:
        limit: Maximum number of entries to display (newest first)
    """
    history = _calculator_history.get_history(limit)
    if not history:
        print("No calculations in history.")
        return

    print(f"\n📊 Calculation History ({len(history)} entries):")
    print("-" * 50)
    for i, entry in enumerate(history, 1):
        timestamp = entry["timestamp"].strftime("%H:%M:%S")
        print(f"{i:2d}. [{timestamp}] {entry['expression']}")


def get_last_calculation_result() -> float | None:
    """Get the result of the last calculation.

    Returns:
        The result of the last calculation, or None if no calculations
    """
    return _calculator_history.get_last_result()


def clear_calculation_history() -> int:
    """Clear all calculation history.

    Returns:
        Number of entries that were cleared
    """
    return _calculator_history.clear_history()


def get_history_count() -> int:
    """Get the total number of calculations in history.

    Returns:
        Number of calculations performed
    """
    return _calculator_history.get_history_count()


def get_history_summary() -> dict[str, Any]:
    """Get a summary of the calculation history.

    Returns:
        Dictionary with history statistics
    """
    history = _calculator_history.get_history()
    if not history:
        return {
            "total_calculations": 0,
            "operations_used": [],
            "most_recent": None,
            "first_calculation": None,
        }

    # Count operations
    operations = {}
    for entry in history:
        op = entry["operation"]
        operations[op] = operations.get(op, 0) + 1

    return {
        "total_calculations": len(history),
        "operations_used": list(operations.keys()),
        "operation_counts": operations,
        "most_recent": history[0]["expression"],
        "first_calculation": history[-1]["expression"],
    }


if __name__ == "__main__":
    print("🧮 Calculator Module with History")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"√16 = {sqrt(16)}")
    print(f"2^3 = {power(2, 3)}")

    # Display history
    print_history()
