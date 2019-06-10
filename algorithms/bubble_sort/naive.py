def bubble_sort(alist):
    """Bubble sort in place"""
    length = len(alist)
    while True:
        swaped = False
        for i in range(length - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swaped = True
        if not swaped:
            break
