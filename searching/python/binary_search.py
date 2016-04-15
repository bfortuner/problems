"""
Binary Search

Write method to return True if integer is in array
"""


def binary_search(arr, val):
	low = 0
	high = len(arr)-1
	while low <= high:
		mid = low + (high-low)/2
		if arr[mid] == val:
			return True
		elif arr[mid] > val:
			high = mid-1
		else:
			low = mid+1
	return False



# Tests
a1 = [1,2,3,4,5]
a2 = [1,2]

def test_binary_search():
	assert binary_search(a1, 2) == True
	assert binary_search(a1, 9) == False
	assert binary_search(a1, 1) == True
	assert binary_search(a1, 0) == False
	
	assert binary_search(a2, 5) == False
	assert binary_search(a2, 1) == True
	assert binary_search(a2, 2) == True
	assert binary_search(a2, -3) == False



if __name__ == "__main__":
	test_binary_search()

