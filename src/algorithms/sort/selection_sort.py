"""
Selection Sort Implementation

Sort a list of numbers by creating a sorted section and an unsorted one.
Find the minimum value of the unsorted section.
Swap it with the leftmost number in the unsorted section.
Push the boundaries of the sorted section to the right.

Time Complexity:
    Worst: O(n ^ 2) - Quadratic
    Average: O(n ^ 2) - Quadratic
    Best: O(n ^ 2) - Quadratic
Space Complexity:
    Worst: O(1) - Constant
"""


def selection_sort(lst):
    """
    Implementation of the selection sort algorithm.

    Input:
        lst: List of numbers (The list to sort)

    Output:
        Sort the list in place, no output
    """

    # The boundary between the sorted and unsorted sections
    boundary = 0

    for _ in range(len(lst) - 1):
        minimum, index = lst[boundary], boundary
        for i in range(boundary, len(lst)):
            if lst[i] < minimum:
                minimum, index = lst[i], i
        lst[boundary], lst[index] = lst[index], lst[boundary]
        boundary += 1
