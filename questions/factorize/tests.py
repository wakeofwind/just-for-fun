from fixtures import FIXTURES
import naive


def _test_impl(impl):
    for number, result in FIXTURES:
        assert impl(number) == result


def test_factorize():
    _test_impl(naive.factorize)


if __name__ == '__main__':
    test_factorize()
