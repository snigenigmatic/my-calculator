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

    print(f"Multiplying {a} × {b}")  # Added logging
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
    try:
        result = a**b
        if result == float("inf"):
            raise OverflowError("Result too large to represent")
        return result
    except OverflowError:
        raise OverflowError("Power operation resulted in overflow")


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
