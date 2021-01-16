"""
Linear Search Implementation

Find an element in a list by checking every element in the list.

Time Complexity:
    Worst: O(n) - Linear
    Average: O(n/2) - Linear
    Best: O(1) - Constant
Space Complexity:
    Worst: O(1) - Constant
"""

ELEMENT_NOT_FOUND = -1


def linear_search(search_list, target):
    """
    Implementation of the linear search algorithm.

    Input:
        search_list: List of items (Usually numbers)
        target: The item to find

    Output:
        Return the index of the target if it is in the list.
        Return -1 otherwise.
    """

    for i, item in enumerate(search_list):
        if item == target:
            return i
    return ELEMENT_NOT_FOUND


def custom_linear_search(items, search_item, are_equal=lambda x, y: x == y):
    """
    Implementation of the linear search algorithm.
    Accepts an optional custom comparing function.

    Input:
        search_list: List of items (Usually numbers)
        target: The item to find
        are_equal: Custom function to determine which items are equal

    Output:
        Return the index of the target if it is in the list.
        Return -1 otherwise.
    """

    for i, item in enumerate(items):
        if are_equal(item, search_item):
            return i
    return ELEMENT_NOT_FOUND
