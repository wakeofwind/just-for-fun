from fixtures import FIXTURES

import naive


def _test_impl(impl):
    for n, result in FIXTURES:
        assert impl(n) == result


def test_find_primes():
    _test_impl(naive.find_primes)


if __name__ == '__main__':
    test_find_primes()
