# Fibonacci numbers
# Traditional recursive fib
from typing import Dict, List


def trad_fib(n):
    if n <= 1:
        return 1
    return trad_fib(n - 1) + trad_fib(n - 2)


# Improve using Memoization
def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """Returns the nth Fibonacci number using memoization.

    Args:
        n: The index of the Fibonacci number to compute.
        memo: A dictionary to store previously computed Fibonacci numbers.

    Returns:
        The nth Fibonacci number.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


# Regular recursive (Slow) solution
# O(2^(m + n)) time
# O(n + m) space
def grid_traveler(m: int, n: int):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


# O(mn)
# O(m + n)
def memo_grid_traveler(m: int, n: int, memo: Dict[tuple[int, int], int] = {}) -> int:
    key = (m, n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = memo_grid_traveler(m - 1, n, memo) + memo_grid_traveler(m, n - 1, memo)
    return memo[key]


# Recursive canSum
# Worst case O(n^m), the longest tree has m elements, each has n children.
def canSum(targetSum: int, numbers: List[int]) -> bool:
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        if canSum(targetSum - num, numbers):
            return True

    return False
