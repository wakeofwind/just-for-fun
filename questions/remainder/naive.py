"""
via http://air.googol.im/post/mod-3/
"""

def remainder(n, p):
    if n < p:
        return n

    m = 0
    maximum = n - p
    while m <= maximum:
        m += p

    return n - m
