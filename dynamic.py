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


def memo_canSum(targetSum, numbers, memo):
    # memo = { targetSum : (bool, list)
    # when true, add targetSum to list
    # you're returning the whole tuple. if memo[0] then add yourself to tuple[1]
    if targetSum in memo:
        return memo[targetSum][0]
    if targetSum == 0:
        return [True, []]
    if targetSum < 0:
        return [False, []]
    for num in numbers:
        if canSum(targetSum - num, numbers):
            memo[targetSum][0] = True
            return True

    memo[targetSum][0] = False
    return False


result = []


def memo_howSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        if memo_howSum(targetSum - num, numbers):
            memo[targetSum] = True
            result.append(num)
            return True

    return False


def howSumVideo(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        rem = targetSum - num
        res = howSumVideo(rem, numbers)
        if res is not None:
            return [*res, num]

    return None


def bestSum(target, numbers):
    # have to check every possibility
    # base case:
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None
    for num in numbers:
        rem = target - num
        combination = bestSum(rem, numbers)
        if combination is not None:
            current_combination = [*combination, num]
            if shortest_combination is None or len(current_combination) < len(shortest_combination):
                shortest_combination = current_combination

    return shortest_combination


def memo_bestSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None
    for num in numbers:
        rem = target - num
        combination = memo_bestSum(rem, numbers, memo)
        if combination is not None:
            current_combination = [*combination, num]
            if shortest_combination is None or len(current_combination) < len(shortest_combination):
                shortest_combination = current_combination

    memo[target] = shortest_combination
    return shortest_combination


def canConstruct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return True
    for word in word_bank:
        if target[:len(word)] == word:
            if canConstruct(target[len(word):], word_bank):
                memo[target] = True
                return True

    memo[target] = False
    return False


def countConstruct(target, wordBank, memo={}):
    # memo: {target: bool}
    # if true, inc counter
    counter = 0
    if target in memo:
        return memo[target]

    if len(target) == 0:
        return 1
    for word in wordBank:
        if target[:len(word)] == word:
            counter += countConstruct(target[len(word):], wordBank, memo)

    memo[target] = counter
    return counter


print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                     ["e", "ee", "eee", "eee", "eeee", "eeeee", "eeeeeee", "eeeeeeeeee"
                      ]))
