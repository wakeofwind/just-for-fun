from fixtures import FIXTURES
import naive


def _test_impl(impl):
    for number, dividend, remainder in FIXTURES:
        assert impl(number, dividend) == remainder


def test_remainder():
    _test_impl(naive.remainder)


if __name__ == '__main__':
    test_remainder()
