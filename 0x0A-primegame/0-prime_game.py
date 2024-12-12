#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the range of numbers for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
             Returns None if there is no winner.
    """
    if not nums or x < 1:
        return None

    # Find the maximum value of n to calculate primes up to this value
    max_n = max(nums)
    
    # Step 1: Use the Sieve of Eratosthenes to find primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)
    
    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes up to n is odd, Maria wins; otherwise, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
