"""
Search Algorithms
"""

def linear_search(items, search_item):
	"""
	Implementation of the linear search algorithm.

	Return the index of the search_item if it is in the list.
	Return -1 otherwise.

	Time Complexity: O(n) "Linear"
	Space Complexity: O(1) "Constant"
	"""
	for i, item in enumerate(items):
		if item == search_item:
			return i
	return -1


