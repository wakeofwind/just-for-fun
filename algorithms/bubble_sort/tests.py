from fixtures import FIXTURES
import naive


def _test_impl(impl):
    for alist, result in FIXTURES:
        impl(alist)
        assert alist == result


def test_bubble_sort():
    _test_impl(naive.bubble_sort)


if __name__ == '__main__':
    test_bubble_sort()
