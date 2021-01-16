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


def binary_search(search_list, target):
    """
    Implementation of the binary search algorithm.

    Input:
        search_list: Sorted list of items (Usually numbers)
        target: The item to find

    Output:
        Return the index of the target if it is in the list.
        Return -1 otherwise.
    """

    start = 0
    end = len(search_list) - 1

    while start <= end:
        mid = start + math.floor((end - start) / 2)
        if search_list[mid] == target:
            return mid
        if search_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return ELEMENT_NOT_FOUND
