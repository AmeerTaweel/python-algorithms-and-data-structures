"""
Insertion Sort Implementation

Sort a list of numbers by looping over the numbers, moving swapping them to the
right place.

Time Complexity:
    Worst: O(n ^ 2) - Quadratic
    Average: O(n ^ 2) - Quadratic
    Best: O(n) - Linear
Space Complexity:
    Worst: O(1) - Constant
"""


def insertion_sort(lst):
    """
    Implementation of the insertion sort algorithm.

    Input:
        lst: List of numbers (The list to sort)

    Output:
        Sort in place, no output.
    """

    for i in range(1, len(lst)):
        ci = i  # Current i
        while ci > 0 and lst[ci] < lst[ci - 1]:
            lst[ci], lst[ci - 1] = lst[ci - 1], lst[ci]
            ci -= 1
