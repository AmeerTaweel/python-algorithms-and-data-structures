"""
Binary Search Implementation

Find an element in a sorted list by checking the middle element.
If the element is the target, return the index.
If the element is larger than the target, discard the left half of the list.
If the element is smaller than the target, discard the right half of the list.
Repeat the same steps for the remaining half of the list.

Time Complexity:
    Worst: O(log n) - Logarithmic
    Average: O(log n) - Logarithmic
    Best: O(1) - Constant
Space Complexity:
    Worst: O(1) - Constant
"""

import math

ELEMENT_NOT_FOUND = -1


def binary_search(items, search_item):
    """
    Implementation of the binary search algorithm.

    Return the index of the search_item if it is in a sorted list.
    The list must be sorted for this to work
    Return -1 otherwise.
    """
    start = 0
    end = len(items) - 1

    while start <= end:
        mid = start + math.floor((end - start) / 2)
        if items[mid] == search_item:
            return mid
        if items[mid] > search_item:
            end = mid - 1
        else:
            start = mid + 1

    return ELEMENT_NOT_FOUND
