"""
HW04 - Repetition utilities

Functions:
- get_factorial(n): returns n! using a for-range loop (n >= 0)
- sum_odd_numbers(limit): sum of all positive odd numbers from 1..limit using a while loop (limit >= 1)
"""

from typing import Final


def get_factorial(n: int) -> int:
    """
    Return n! computed with a for-range loop.

    Parameters
    ----------
    n : int
        Integer >= 0.

    Returns
    -------
    int
        Factorial of n.

    Raises
    ------
    TypeError
        If n is not an int.
    ValueError
        If n < 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be >= 0")

    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sum_odd_numbers(limit: int) -> int:
    """
    Return the sum of all positive odd numbers from 1 up to and including `limit`.
    Uses a while loop.

    Examples:
    - limit=10 -> 1+3+5+7+9 = 25
    - limit=1  -> 1

    Parameters
    ----------
    limit : int
        Integer >= 1.

    Returns
    -------
    int
        Sum of odd numbers 1..limit inclusive.

    Raises
    ------
    TypeError
        If limit is not an int.
    ValueError
        If limit < 1.
    """
    if not isinstance(limit, int):
        raise TypeError("limit must be an int")
    if limit < 1:
        raise ValueError("limit must be >= 1")

    total: int = 0
    current: int = 1
    while current <= limit:
        total += current
        current += 2
    return total
