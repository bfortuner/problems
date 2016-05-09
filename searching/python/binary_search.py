"""
Binary Search

Write method to return True if integer is in array
"""


def binary_search(arr, val):
	low = 0
	high = len(arr)-1
	while low <= high:
		mid = low + (high-low)/2  #alternatively (high+low)/2
		if arr[mid] == val:
			return True
		elif arr[mid] < val:
			low = mid+1
		else:
			high = mid-1
	return False


def binary_search_recur(arr, val):
	if arr is None or len(arr) == 0:
		return False
	mid = len(arr)/2
	if arr[mid] == val:
		return True
	elif arr[mid] > val:
		return binary_search_recur(arr[:mid], val)
	else:
		return binary_search_recur(arr[mid+1:], val)




# Tests
a1 = [1,2,3,4,5]
a2 = [1,2]
a3 = [1]

def test_binary_search():
	assert binary_search(a1, 2) == True
	assert binary_search(a1, 9) == False
	assert binary_search(a1, 1) == True
	assert binary_search(a1, 0) == False
	
	assert binary_search(a2, 5) == False
	assert binary_search(a2, 1) == True
	assert binary_search(a2, 2) == True
	assert binary_search(a2, -3) == False

	assert binary_search(a3, 1) == True
	assert binary_search(a3, 0) == False
	assert binary_search(a3, 3) == False

def test_binary_search_recur():
	assert binary_search_recur(a1, 2) == True
	assert binary_search_recur(a1, 9) == False
	assert binary_search_recur(a1, 1) == True
	assert binary_search_recur(a1, 0) == False
	
	assert binary_search_recur(a2, 5) == False
	assert binary_search_recur(a2, 1) == True
	assert binary_search_recur(a2, 2) == True
	assert binary_search_recur(a2, -3) == False

	assert binary_search_recur(a3, 1) == True
	assert binary_search_recur(a3, 0) == False
	assert binary_search_recur(a3, 3) == False

if __name__ == "__main__":
	test_binary_search()
	test_binary_search_recur()

