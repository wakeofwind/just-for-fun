"""Find primes in naive implementation"""


def find_primes(n):
    """Find primes less than N."""
    primes = [] if n < 3 else [2]

    i = 3
    while i < n:
        for p in primes:
            if not i % p:
                break
        else:
            primes.append(i)
        i += 1

    return primes
