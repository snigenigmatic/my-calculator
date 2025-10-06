# 🧮 Calculator with History

A Python calculator module with comprehensive calculation history tracking. This calculator supports basic arithmetic operations and maintains a detailed history of all calculations performed.

## Features

### Basic Operations
- **Addition** (`add(a, b)`) - Add two numbers
- **Subtraction** (`subtract(a, b)`) - Subtract b from a  
- **Multiplication** (`multiply(a, b)`) - Multiply two numbers
- **Division** (`divide(a, b)`) - Divide a by b with zero-division protection
- **Power** (`power(a, b)`) - Raise a to the power of b with overflow protection
- **Square Root** (`sqrt(a)`) - Calculate square root with negative input protection

### History Features 🆕
- **Automatic History Tracking** - All successful calculations are automatically recorded
- **Detailed History Entries** - Each entry includes operation, operands, result, timestamp, and formatted expression
- **History Management** - View, limit, clear, and summarize calculation history
- **Chronological Ordering** - History is maintained in chronological order (newest first)
- **Error Exclusion** - Failed calculations are not recorded in history

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd my-calculator

# Install dependencies
pip install -r requirements.txt

# Or using uv (recommended)
uv sync
```

## Usage

### Basic Calculator Operations

```python
from src.calculator import add, subtract, multiply, divide, power, sqrt

# Basic arithmetic
result = add(5, 3)        # Returns 8
result = subtract(10, 4)  # Returns 6  
result = multiply(6, 7)   # Returns 42
result = divide(15, 3)    # Returns 5.0
result = power(2, 3)      # Returns 8
result = sqrt(16)         # Returns 4.0
```

### History Management

```python
from src.calculator import (
    add, multiply, sqrt,
    get_calculation_history,
    print_history,
    get_last_calculation_result,
    clear_calculation_history,
    get_history_count,
    get_history_summary
)

# Perform some calculations
add(5, 3)
multiply(4, 6) 
sqrt(25)

# View calculation history
print_history()
# Output:
# 📊 Calculation History (3 entries):
# --------------------------------------------------
#  1. [14:32:15] √25 = 5.0
#  2. [14:32:10] 4 x 6 = 24
#  3. [14:32:05] 5 + 3 = 8

# Get history programmatically
history = get_calculation_history(limit=2)  # Get last 2 calculations
for entry in history:
    print(f"{entry['expression']} at {entry['timestamp']}")

# Get last result
last_result = get_last_calculation_result()  # Returns 5.0

# Get history statistics
summary = get_history_summary()
print(f"Total calculations: {summary['total_calculations']}")
print(f"Operations used: {summary['operations_used']}")

# Clear history
cleared_count = clear_calculation_history()
print(f"Cleared {cleared_count} entries")
```

### Command Line Usage

```python
# Run the calculator module directly
python src/calculator.py

# Output will show example calculations and history:
# 🧮 Calculator Module with History
# 2 + 3 = 5
# 5 - 2 = 3
# Multiplying 4 x 6
# Result: 24
# 4 * 6 = 24
# Dividing 10 ÷ 2
# Result: 5.0
# 10 / 2 = 5.0
# √16 = 4.0
# 2^3 = 8
#
# 📊 Calculation History (6 entries):
# --------------------------------------------------
#  1. [14:35:20] 2 ^ 3 = 8
#  2. [14:35:20] √16 = 4.0
#  3. [14:35:20] 10 ÷ 2 = 5.0
#  4. [14:35:20] 4 x 6 = 24
#  5. [14:35:20] 5 - 2 = 3
#  6. [14:35:20] 2 + 3 = 5
```

## API Reference

### History Functions

#### `get_calculation_history(limit=None)`
Returns the calculation history as a list of dictionaries.

**Parameters:**
- `limit` (int, optional): Maximum number of entries to return (newest first)

**Returns:**
- `list[dict]`: List of history entries with keys: `operation`, `operands`, `result`, `timestamp`, `expression`

#### `print_history(limit=None)`
Prints the calculation history in a human-readable format.

**Parameters:**
- `limit` (int, optional): Maximum number of entries to display

#### `get_last_calculation_result()`
Returns the result of the most recent calculation.

**Returns:**
- `float | None`: Last calculation result, or None if no calculations

#### `clear_calculation_history()`
Clears all calculation history.

**Returns:**
- `int`: Number of entries that were cleared

#### `get_history_count()`
Returns the total number of calculations in history.

**Returns:**
- `int`: Number of calculations performed

#### `get_history_summary()`
Returns statistical summary of calculation history.

**Returns:**
- `dict`: Summary with keys: `total_calculations`, `operations_used`, `operation_counts`, `most_recent`, `first_calculation`

## Error Handling

The calculator includes comprehensive error handling:

- **Type Validation**: All functions validate input types and raise `TypeError` for non-numeric inputs
- **Division by Zero**: `divide()` raises `ValueError` for zero divisors
- **Negative Square Root**: `sqrt()` raises `ValueError` for negative inputs  
- **Power Overflow**: `power()` raises `OverflowError` for calculations that would be too large
- **History Isolation**: Failed calculations are not recorded in history

## Development

### Running Tests

```bash
# Run all tests
pytest tests/unit/ -v

# Run specific test files
pytest tests/unit/test_calculator.py -v      # Original calculator tests
pytest tests/unit/test_history.py -v        # History feature tests

# Run with coverage
pytest tests/unit/ --cov=src --cov-report=html
```

### Linting and Formatting

```bash
# Check for linting issues
ruff check src/ tests/

# Fix auto-fixable issues
ruff check src/ tests/ --fix

# Format code
ruff format src/ tests/

# Check if code is already formatted
ruff format src/ tests/ --check
```

### Project Structure

```
my-calculator/
├── src/
│   ├── __init__.py
│   └── calculator.py          # Main calculator module with history
├── tests/
│   ├── __init__.py
│   └── unit/
│       ├── __init__.py
│       ├── test_calculator.py # Original calculator tests
│       └── test_history.py    # History functionality tests
├── pyproject.toml             # Project configuration and dependencies
├── pytest.ini                # Test configuration
├── requirements.txt           # Dependencies list
└── README.md                  # This file
```

## Contributing

1. Create a new branch for your feature
2. Add comprehensive tests for any new functionality
3. Ensure all tests pass: `pytest tests/unit/ -v`
4. Follow code style guidelines: `ruff check src/ tests/`
5. Update documentation as needed

## History Feature Details

The history feature automatically tracks all successful calculator operations:

- **Entry Format**: Each history entry contains operation name, input operands, result, timestamp, and formatted expression
- **Automatic Tracking**: No manual intervention required - all calculator functions automatically record their operations
- **Error Resilience**: Failed operations (type errors, division by zero, etc.) are not recorded
- **Memory Efficient**: History is stored in memory for the session duration
- **Flexible Access**: Multiple ways to access and view history data

### History Entry Structure

```python
{
    'operation': 'add',           # Operation name
    'operands': [5, 3],          # Input values
    'result': 8,                 # Calculation result  
    'timestamp': datetime(...),   # When calculation was performed
    'expression': '5 + 3 = 8'    # Human-readable format
}
```