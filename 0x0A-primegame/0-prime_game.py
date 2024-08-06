#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def prime_numbers(n):
    """
    Return a list of prime numbers between 1 and n
    inclusive using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): Upper boundary of the range (inclusive).

    Returns:
        list: A list of prime numbers between 1 and n inclusive.
    """
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, n + 1, start):
                sieve[multiple] = False

    return [num for num in range(2, n + 1) if sieve[num]]


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds of the game.
        nums (list): List of upper limits for each round.

    Returns:
        str: Name of the winner ("Maria" or "Ben") or
        None if no winner can be determined.
    """
    if not x or not nums:
        return None

    maria_score = 0
    ben_score = 0

    for i in range(x):
        prime_count = len(prime_numbers(nums[i]))
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    return None
