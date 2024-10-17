#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Return a list where prime[i] is True if i is prime, False otherwise."""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def isWinner(x, nums):
    """Determine the winner of the most rounds."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Memoize the number of moves for each n
    prime_moves = [0] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + primes[i]
    
    maria_wins = 0
    ben_wins = 0
    
    # Simulate each round
    for n in nums:
        if prime_moves[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
