#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.
    """
    # Check for invalid input
    if x <= 0 or not nums or x != len(nums):
        return None
    
    # Initialize scores
    ben = 0
    maria = 0
    
    # Get the maximum number in nums to create a prime sieve
    max_n = max(nums)
    
    # Sieve of Eratosthenes to mark primes
    primes = [True] * (max_n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Convert the boolean prime list into a cumulative sum list
    # prime_count[i] tells how many primes exist up to number i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Simulate each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
