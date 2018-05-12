""" The first quick and dirty try. """


def factorize(number):
    """ Factorize a positive integer.

    e.g. 270 = 2 * 3 * 3 * 3 * 5
    """
    if number == 1:
        return [1]

    result = []
    q = 2
    r = number
    while q <= number:
        while not r % q:
            r = r / q
            result.append(q)
        q += 1
    return result
