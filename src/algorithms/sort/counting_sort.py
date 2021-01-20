"""
Counting Sort Implementation

Sort a list of numbers, provided the maximum value of each number.
The numbers should be non negative.

Time Complexity:
    Worst: O(n + k) where k is the maximum value
Space Complexity:
    Worst: O(n + k) where k is the maximum value
"""


def counting_sort(lst, maximum):
    """
    Implementation of the counting sort algorithm.

    Input:
        lst: List of non negative numbers (The list to sort)
        maximum: The max value of any number in the list

    Output:
        A sorted list
    """

    indexes = [0] * (maximum + 1)

    # Count the occurrences of each value and put them in the indexes list
    for i in lst:
        indexes[i] += 1

    # Add the indexes to the next ones
    for i in range(len(indexes) - 1):
        indexes[i + 1] += indexes[i]

    # Shift the indexes one element to the right, in reverse
    for i in range(len(indexes) - 1, 0, -1):
        indexes[i] = indexes[i - 1]
    indexes[0] = 0

    sorted_list = [0] * len(lst)

    # Loop over the list and sort based on index
    for i in lst:
        sorted_list[indexes[i]] = i
        indexes[i] += 1

    return sorted_list
