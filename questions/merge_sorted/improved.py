""" Improved via https://github.com/nryoung/algorithms/blob/master/algorithms/sorting/merge_sort.py . """


def merge_sorted(seq1, seq2):
    """ Merge two sorted list to a new sorted list. """
    result = []
    m = 0
    n = 0
    while m < len(seq1) and n < len(seq2):
        if seq1[m] < seq2[n]:
            result.append(seq1[m])
            m += 1
        else:
            result.append(seq2[n])
            n += 1

    result += seq1[m:]
    result += seq2[n:]

    return result
