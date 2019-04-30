#include <assert.h>

#include "naive.h"

int test_normal()
{
    int array[] = {1, 3, 4, 5, 7, 8, 12, 14, 19, 20};
    int array_length = (int) (sizeof(array) / sizeof(array[0]));
    //printf("array length: %d\n", array_length);
    int i = 0;
    for (; i < array_length; i++) {
        int value = array[i];
        int result = binary_search(array, array_length, value);
        //printf("%d at %d\n", value, result);
        assert(result == i);
    }
    return 0;
}

int test_not_found()
{
    int array[] = {1, 3, 4, 5, 7, 8, 12, 14, 19, 20};
    int array_length = (int) (sizeof(array) / sizeof(array[0]));
    int result;
    result = binary_search(array, array_length, 6);
    assert(result == -1);
    result = binary_search(array, array_length, 100);
    assert(result == -1);

    return 0;
}

int test_empty_array()
{
    int array1[] = {};
    int result1 = binary_search(array1, 0, 6);
    assert(result1 == -1);

    return 0;
}

int test_only_one_element_in_array()
{
    int array2[] = {8};
    int result21 = binary_search(array2, 1, 8);
    assert(result21 == 0);
    int result22 = binary_search(array2, 1, 1024);
    assert(result22 == -1);

    return 0;
}

int test_odd_count_of_elements_in_array()
{
    int array3[] = {2, 6, 15, 42, 71};
    int result31 = binary_search(array3, 5, 42);
    assert(result31 == 3);
    int result32 = binary_search(array3, 5, 22);
    assert(result32 == -1);

    return 0;
}

int main() {
    test_normal();
    test_not_found();
    test_empty_array();
    test_only_one_element_in_array();
    test_odd_count_of_elements_in_array();

    return 0;
}
