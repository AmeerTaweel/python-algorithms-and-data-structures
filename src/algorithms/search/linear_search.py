"""
Linear Search Implementations

Time Complexity:
	Worst: O(n) "Linear"
	Average: O(n/2)
	Best: O(1)
Space Complexity:
	Worst: O(1) "Constant"
"""

ELEMENT_NOT_FOUND = -1

def linear_search(items, search_item, are_equal = lambda x, y: x == y):
	"""
	Implementation of the linear search algorithm.

	Accepts an optional custom comparing function.

	Return the index of the search_item if it is in the list.
	Return -1 otherwise.
	"""
	for i, item in enumerate(items):
		if are_equal(item, search_item):
			return i
	return ELEMENT_NOT_FOUND
