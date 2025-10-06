"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(a, b):
    """Add two numbers together"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    print(f"Multiplying {a} x {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
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
        return result


def sqrt(a):
    """Return the square root of a"""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    return a**0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
