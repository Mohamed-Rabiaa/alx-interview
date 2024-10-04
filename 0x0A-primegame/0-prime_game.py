#!/usr/bin/python3
"""
This module contains the isWinner function
"""


def isWinner(x, nums):
    """
    Determines the winner of a series of rounds in a prime-number removal game
    between two players, Maria and Ben. The game consists of taking turns to
    pick a prime number and removing that prime and its multiples from a set
    of consecutive integers from 1 to n. Maria always goes first, and both
    players play optimally. The player unable to make a move loses the game.

    Args:
    ----------
    x : int
        The number of rounds to be played.
    nums : List[int]
        A list where each element `n` represents the range of integers (1 to n)
        for each round.

    Returns:
    -------
    str or None
        Returns "Maria" if Maria wins more rounds, "Ben" if Ben wins
        more rounds, or None if there is no clear winner (i.e., both
        win an equal number of rounds).
    """
    # Step 1: Precompute primes up to 10000 using Sieve of Eratosthenes
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Step 2: Precompute the winning counts for Maria
    # win_count[n] will store if Maria wins (1) or Ben wins (0) when n is given
    win_count = [0] * (max_n + 1)

    for n in range(2, max_n + 1):
        moves = 0
        remaining = [True] * (n + 1)

        # Count moves by marking primes and their multiples
        for i in range(2, n + 1):
            if remaining[i] and is_prime[i]:  # Pick prime if available
                moves += 1  # Each prime pick is a move
                for multiple in range(i, n + 1, i):
                    remaining[multiple] = False  # Mark multiples as removed

        # Maria wins if moves is odd, Ben wins if moves is even
        win_count[n] = 1 if moves % 2 == 1 else 0

    # Step 3: Calculate wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if win_count[n] == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
