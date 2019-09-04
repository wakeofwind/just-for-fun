"""Find primes in naive implementation"""


def find_primes(n):
    """Find primes smaller than N."""
    primes = [] if n < 3 else [2]

    i = 3
    while i < n:
        for p in primes:
            if not i % p:
                break
        else:
            primes.append(i)
        i += 2

    return primes
