"""Multifunction calculator"""


def check_number(value: object, name: str) -> None:
    """Raise TypeError if value is not a number (int or float)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(name + " must be a number.")


def add(a: float, b: float) -> float:
    """Return the sum of a and b.

    Raises:
        TypeError: If a or b is not a number
    """
    check_number(a, "a")
    check_number(b, "b")
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b.

    Raises:
        TypeError: If a or b is not a number
    """
    check_number(a, "a")
    check_number(b, "b")
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    check_number(a, "a")
    check_number(b, "b")
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: Dividend
        b: Divisor (must not be zero)

    Returns:
        Result as a float

    Raises:
        TypeError: If a or b is not a number
        ValueError: If b is zero
    """
    check_number(a, "a")
    check_number(b, "b")
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("subtract(10, 4) =", subtract(10, 4))
    print("multiply(3, 4) =", multiply(3, 4))
    print("divide(6, 3) =", divide(6, 3))