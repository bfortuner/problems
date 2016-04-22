
"""
Bubble Sort

Loops Through Swapping Each out-of-order
value with its neighbor until all values
are in order

Worst Case: O(n^2)
Best Case: O(n)
"""

def sort(arr):
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		i = 0
		while i < len(arr):
			cur = arr[i]
			#we have found something out of order
			if i+1 < len(arr) and cur > arr[i+1]:
				is_sorted = False
				arr[i] = arr[i+1]
				arr[i+1] = cur
			i+=1
	return arr



if __name__ == "__main__":
	assert sort([3,2,5,5]) == [2,3,5,5]
	assert sort([3,2,5]) == [2,3,5]
	assert sort([2,1]) == [1,2]
	assert sort([1,2]) == [1,2]
	assert sort([1]) == [1]
	assert sort([]) == []
	assert sort([1,2,3,4]) == [1,2,3,4]
	assert sort(["A","C","B"]) == ["A","B","C"]
	assert sort([2,3,5,2,5,5]) == [2,2,3,5,5,5]
	assert sort([2,3,5,-2,5,5]) == [-2,2,3,5,5,5]
