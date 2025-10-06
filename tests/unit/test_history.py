"""
Test history functionality for the calculator
"""

from datetime import datetime

import pytest

from src.calculator import (
    _calculator_history,
    add,
    clear_calculation_history,
    divide,
    get_calculation_history,
    get_history_count,
    get_history_summary,
    get_last_calculation_result,
    multiply,
    power,
    print_history,
    sqrt,
    subtract,
)


class TestHistoryBasics:
    """Test basic history functionality."""

    def setup_method(self):
        """Clear history before each test."""
        clear_calculation_history()

    def test_history_starts_empty(self):
        """Test that history starts empty."""
        assert get_history_count() == 0
        assert get_calculation_history() == []
        assert get_last_calculation_result() is None

    def test_add_operation_recorded(self):
        """Test that add operations are recorded in history."""
        result = add(5, 3)
        assert result == 8
        assert get_history_count() == 1

        history = get_calculation_history()
        assert len(history) == 1
        entry = history[0]
        assert entry["operation"] == "add"
        assert entry["operands"] == [5, 3]
        assert entry["result"] == 8
        assert entry["expression"] == "5 + 3 = 8"
        assert isinstance(entry["timestamp"], datetime)

    def test_subtract_operation_recorded(self):
        """Test that subtract operations are recorded in history."""
        result = subtract(10, 4)
        assert result == 6

        history = get_calculation_history()
        entry = history[0]
        assert entry["operation"] == "subtract"
        assert entry["operands"] == [10, 4]
        assert entry["result"] == 6
        assert entry["expression"] == "10 - 4 = 6"

    def test_multiply_operation_recorded(self):
        """Test that multiply operations are recorded in history."""
        result = multiply(6, 7)
        assert result == 42

        history = get_calculation_history()
        entry = history[0]
        assert entry["operation"] == "multiply"
        assert entry["operands"] == [6, 7]
        assert entry["result"] == 42
        assert entry["expression"] == "6 x 7 = 42"

    def test_divide_operation_recorded(self):
        """Test that divide operations are recorded in history."""
        result = divide(15, 3)
        assert result == 5.0

        history = get_calculation_history()
        entry = history[0]
        assert entry["operation"] == "divide"
        assert entry["operands"] == [15, 3]
        assert entry["result"] == 5.0
        assert entry["expression"] == "15 ÷ 3 = 5.0"

    def test_power_operation_recorded(self):
        """Test that power operations are recorded in history."""
        result = power(2, 3)
        assert result == 8

        history = get_calculation_history()
        entry = history[0]
        assert entry["operation"] == "power"
        assert entry["operands"] == [2, 3]
        assert entry["result"] == 8
        assert entry["expression"] == "2 ^ 3 = 8"

    def test_sqrt_operation_recorded(self):
        """Test that sqrt operations are recorded in history."""
        result = sqrt(16)
        assert result == 4.0

        history = get_calculation_history()
        entry = history[0]
        assert entry["operation"] == "sqrt"
        assert entry["operands"] == [16]
        assert entry["result"] == 4.0
        assert entry["expression"] == "√16 = 4.0"


class TestHistoryManagement:
    """Test history management functions."""

    def setup_method(self):
        """Clear history before each test."""
        clear_calculation_history()

    def test_multiple_operations_chronological_order(self):
        """Test that multiple operations are stored in chronological order."""
        add(1, 2)  # Should be oldest
        subtract(5, 3)
        multiply(4, 5)  # Should be newest

        history = get_calculation_history()
        assert len(history) == 3

        # History should be returned newest first
        assert history[0]["expression"] == "4 x 5 = 20"
        assert history[1]["expression"] == "5 - 3 = 2"
        assert history[2]["expression"] == "1 + 2 = 3"

    def test_get_last_calculation_result(self):
        """Test getting the last calculation result."""
        assert get_last_calculation_result() is None

        add(3, 4)
        assert get_last_calculation_result() == 7

        multiply(2, 5)
        assert get_last_calculation_result() == 10

    def test_clear_history(self):
        """Test clearing history."""
        add(1, 1)
        add(2, 2)
        add(3, 3)

        assert get_history_count() == 3
        cleared_count = clear_calculation_history()

        assert cleared_count == 3
        assert get_history_count() == 0
        assert get_calculation_history() == []
        assert get_last_calculation_result() is None

    def test_history_limit(self):
        """Test limiting the number of history entries returned."""
        for i in range(5):
            add(i, i)

        assert get_history_count() == 5

        # Test with limit
        limited_history = get_calculation_history(limit=3)
        assert len(limited_history) == 3

        # Should return the 3 most recent (newest first)
        assert limited_history[0]["expression"] == "4 + 4 = 8"
        assert limited_history[1]["expression"] == "3 + 3 = 6"
        assert limited_history[2]["expression"] == "2 + 2 = 4"

    def test_history_summary(self):
        """Test getting history summary."""
        # Test empty history
        summary = get_history_summary()
        assert summary["total_calculations"] == 0
        assert summary["operations_used"] == []
        assert summary["most_recent"] is None
        assert summary["first_calculation"] is None

        # Add some operations
        add(1, 2)
        multiply(3, 4)
        add(5, 6)
        sqrt(9)

        summary = get_history_summary()
        assert summary["total_calculations"] == 4
        assert set(summary["operations_used"]) == {"add", "multiply", "sqrt"}
        assert summary["operation_counts"]["add"] == 2
        assert summary["operation_counts"]["multiply"] == 1
        assert summary["operation_counts"]["sqrt"] == 1
        assert summary["most_recent"] == "√9 = 3.0"
        assert summary["first_calculation"] == "1 + 2 = 3"


class TestHistoryEdgeCases:
    """Test edge cases for history functionality."""

    def setup_method(self):
        """Clear history before each test."""
        clear_calculation_history()

    def test_failed_operations_not_recorded(self):
        """Test that failed operations are not recorded in history."""
        initial_count = get_history_count()

        # Test division by zero
        with pytest.raises(ValueError):
            divide(10, 0)

        # Test invalid type
        with pytest.raises(TypeError):
            add("not", "numbers")

        # Test negative sqrt
        with pytest.raises(ValueError):
            sqrt(-4)

        # Test power overflow
        with pytest.raises(OverflowError):
            power(2, 1000000)

        # History count should not have changed
        assert get_history_count() == initial_count

    def test_history_with_negative_numbers(self):
        """Test history with negative numbers."""
        add(-5, -3)
        subtract(-10, -7)
        multiply(-2, 4)

        history = get_calculation_history()
        assert len(history) == 3
        assert history[2]["expression"] == "-5 + -3 = -8"
        assert history[1]["expression"] == "-10 - -7 = -3"
        assert history[0]["expression"] == "-2 x 4 = -8"

    def test_history_with_floating_point_numbers(self):
        """Test history with floating point numbers."""
        add(1.5, 2.7)
        divide(7, 3)

        history = get_calculation_history()
        assert len(history) == 2
        assert "1.5 + 2.7 = 4.2" in history[1]["expression"]
        assert "7 ÷ 3 =" in history[0]["expression"]

    def test_print_history_empty(self, capsys):
        """Test printing empty history."""
        print_history()
        captured = capsys.readouterr()
        assert "No calculations in history." in captured.out

    def test_print_history_with_data(self, capsys):
        """Test printing history with data."""
        add(2, 3)
        multiply(4, 5)

        print_history()
        captured = capsys.readouterr()
        assert "Calculation History (2 entries)" in captured.out
        assert "4 x 5 = 20" in captured.out
        assert "2 + 3 = 5" in captured.out

    def test_print_history_with_limit(self, capsys):
        """Test printing history with limit."""
        add(1, 1)
        add(2, 2)
        add(3, 3)

        print_history(limit=2)
        captured = capsys.readouterr()
        assert "Calculation History (2 entries)" in captured.out
        assert "3 + 3 = 6" in captured.out
        assert "2 + 2 = 4" in captured.out
        assert "1 + 1 = 2" not in captured.out


class TestHistoryDataIntegrity:
    """Test data integrity of history entries."""

    def setup_method(self):
        """Clear history before each test."""
        clear_calculation_history()

    def test_history_entries_consistent(self):
        """Test that history entries are consistently formatted."""
        add(5, 3)

        # Get history multiple times
        history1 = get_calculation_history()
        history2 = get_calculation_history()

        # Should have same content
        assert len(history1) == len(history2) == 1
        assert history1[0]["expression"] == history2[0]["expression"]
        assert history1[0]["operation"] == history2[0]["operation"]
        assert history1[0]["operands"] == history2[0]["operands"]
        assert history1[0]["result"] == history2[0]["result"]

    def test_operands_list_copied(self):
        """Test that operands list is properly copied."""
        operands = [1, 2]
        _calculator_history.add_entry("test", operands, 3)

        # Modify original operands
        operands[0] = 999

        # Verify history wasn't affected
        history = get_calculation_history()
        assert history[0]["operands"] == [1, 2]

    def test_timestamp_accuracy(self):
        """Test that timestamps are accurate."""
        before = datetime.now()
        add(1, 1)
        after = datetime.now()

        history = get_calculation_history()
        timestamp = history[0]["timestamp"]

        assert before <= timestamp <= after
