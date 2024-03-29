#!/usr/bin/python3
"""Module that finds a peak in a list of integer"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Your algorithm must have the lowest complexity.
    Note: there may be more than one peak in the list.

    The most naive solution to this is to just go through each element
    one-by-one and see if it's qualified as a peak. This solution will take
    O(n) time complexity at the worst case and O(1) for space complexity
    which is super for most algorithm problem. So, here comes the tricky
    part, solve it with O(log(n)) time complexity!

    Usually Binary Search is being used in sorted array(it could also mean
    Bitonic array, or array that's sorted in some other ways), but this
    one is a little bit different as we can't sort the array.

    Returns:
        int: peak(s)
    """
    my_list = list_of_integers
    # if there is no list of integers return None
    if my_list == []:
        return None
    length = len(my_list)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if my_list[mid] > my_list[mid - 1] and my_list[mid] > my_list[mid + 1]:
            return my_list[mid]
        if my_list[mid - 1] > my_list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return my_list[start]
