#!/usr/bin/python3

def isWinner(x, nums):
    # Determines all primes up to the maximum number in nums
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Determines the largest n needed to be handled
    max_n = max(nums)

    # Get prime information up to the maximum n
    is_prime = sieve_of_eratosthenes(max_n)

    # number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                primes_count += 1

        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
