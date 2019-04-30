#include <stdio.h>

#include "naive.h"

/* Return the first element found on the left, else return -1.
   (e.g. array {1, 2, 2, 2, 4, 5} and value 2 then result is 1)
 */
int binary_search(int array[], int array_length, int value)
{
    if (array_length < 1) return -1;

    int high = array_length;
    int low = 0;
    while (low < high)
    {
        //printf("before: low %d high %d\n", low, high);
        int middle = (int) ((high + low) / 2);
        if (array[middle] < value) low = middle + 1;
        else high = middle;
        //printf("after: low %d high %d\n", low, high);
    }

    if (array[low] == value) return low;
    else return -1;
}
