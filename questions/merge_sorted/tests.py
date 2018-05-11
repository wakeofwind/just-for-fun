from fixtures import FIXTURES

import naive
import improved


def _test_impl(impl):
    for seq1, seq2, result in FIXTURES:
        assert impl(seq1, seq2) == result


def test_merge_sorted():
    _test_impl(naive.merge_sorted)
    _test_impl(improved.merge_sorted)


if __name__ == '__main__':
    test_merge_sorted()
