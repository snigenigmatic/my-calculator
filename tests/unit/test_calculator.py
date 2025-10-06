"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""

import pytest

from src.calculator import add, divide, multiply, power, sqrt, subtract


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, 4) == -14


class TestMultiplyDivide:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestPowerSqrt:
    """Test power and square root functions with edge cases."""

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(2, "3")

    def test_power_overflow(self):
        """Test power handles overflow correctly."""
        with pytest.raises(OverflowError, match="Result too large to represent"):
            power(2.0, 1000000)

    def test_sqrt_input_validation(self):
        """Test sqrt rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Argument must be a number"):
            sqrt("16")

    def test_sqrt_negative_input(self):
        """Test sqrt rejects negative inputs."""
        with pytest.raises(
            ValueError, match="Cannot compute square root of negative number"
        ):
            sqrt(-4)


# TODO: Students will add TestMultiplyDivide class
