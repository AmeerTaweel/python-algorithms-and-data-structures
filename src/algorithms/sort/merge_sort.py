"""
Merge Sort Implementation

Sort a list of numbers by continuously splitting it into halves.
Sort the smaller list, and the larger ones, and so on.

Time Complexity:
    Worst: O(n log n) - Linearithmic
    Average: O(n log n) - Linearithmic
    Best: O(n log n) - Linearithmic
Space Complexity:
    Worst: O(n) - Linear
"""


def merge_lists(lst1, lst2):
    """
    Merge two sorted lists into one sorted list.

    Input:
        lst1: Sorted list of numbers
        lst2: Sorted list of numbers

    Output:
        A new sorted list that contains all the elements of both lists
    """

    merged_list = []

    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    if i < len(lst1):
        merged_list += lst1[i:]
    elif j < len(lst2):
        merged_list += lst2[j:]

    return merged_list


def merge_sort(lst):
    """
    Implementation of the merge sort algorithm.

    Input:
        lst: List of numbers (The list to sort)

    Output:
        Sorted list
    """

    length = len(lst)

    if length in (0, 1):
        return lst

    mid = length // 2

    return merge_lists(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
