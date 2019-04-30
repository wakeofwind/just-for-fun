#include <stdio.h>

#include "naive.h"

int binary_search(int array[], int array_length, int value)
{
    if (array_length < 1) return -1;

    int high = array_length;
    int low = 0;
    int middle;
    while (low < high)
    {
        //printf("before: low %d high %d\n", low, high);
        middle = (int) ((high + low) / 2);
        if (array[middle] == value) break;
        else if (array[middle] < value) low = middle + 1;
        else high = middle;
        //printf("after: low %d high %d\n", low, high);
    }

    if (array[middle] == value) return middle;
    else return -1;
}
