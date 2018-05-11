""" The first quick and dirty try. """


def merge_sorted(seq1, seq2):
    """ Merge two sorted list to a new sorted list. """
    result = []
    iter1 = iter(seq1)
    iter2 = iter(seq2)
    stop1 = False
    stop2 = False
    next_who = None
    while True:
        if not next_who or next_who == 1:
            try:
                i = next(iter1)
            except StopIteration:
                stop1 = True
        if not next_who or next_who == 2:
            try:
                j = next(iter2)
            except StopIteration:
                stop2 = True

        if stop1 and stop2:
            break

        if stop1:
            result.append(j)
            next_who = 2
        elif stop2:
            result.append(i)
            next_who = 1
        elif i == j:
            result.append(i)
            result.append(j)
            next_who = None
        elif i < j:
            result.append(i)
            next_who = 1
        elif i > j:
            result.append(j)
            next_who = 2

    return result
