#!/usr/bin/python3
"""Program that performs prime game."""


def isWinner(x, nums):
    """Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of ints rep. range of nos for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
             Returns None if there is no clear winner.
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    # Step 1: Precompute prime numbers using Sieve of Eratosthenes
    is_prime = [True for _ in range(max(n + 1, 2))]
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Step 2: Precompute the cumulative count of primes
    prime_count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_count += 1
        is_prime[i] = prime_count

    # Step 3: Determine the winner for each round
    maria_wins = 0
    for n in nums:
        # Maria wins if the count of primes is odd
        if is_prime[n] % 2 == 1:
            maria_wins += 1

    # Step 4: Determine the overall winner
    total_rounds = len(nums)
    if maria_wins * 2 == total_rounds:
        return None
    if maria_wins * 2 > total_rounds:
        return "Maria"
    return "Ben"
