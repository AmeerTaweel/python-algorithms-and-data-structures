"""
Bubble Sort Implementation

Sort a list of numbers by looping over the list, and bubbling the ith largest
element to the end of the list.

Time Complexity:
    Worst: O(n ^ 2) - Quadratic
    Average: O(n ^ 2) - Quadratic
    Best: O(n) - Linear
Space Complexity:
    Worst: O(1) - Constant
"""


def bubble_sort(lst):
    """
    Implementation of the bubble sort algorithm.

    Input:
        lst: List of numbers (The list to sort)

    Output:
        Sort the list in place, no output
    """

    for _ in range(len(lst)):
        num_of_swaps = 0
        for i in range(len(lst) - 1):
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                num_of_swaps += 1
        if num_of_swaps == 0:
            break
