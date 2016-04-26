
"""
Merge Sort

1. Divide the unsorted list into n sublists, 
each containing 1 element (a list of 1 element is considered sorted).

2. Repeatedly merge sublists to produce new sorted sublists until 
there is only 1 sublist remaining. This will be the sorted list.

Worst Case - O(n Log n)
Best Case - O(n Log n)
"""

def sort(arr):
	if len(arr) == 0:
		return []
	elif len(arr) == 1:
		return arr
	else:
		midpoint = len(arr)/2
		return merge(sort(arr[:midpoint]), 
			sort(arr[midpoint:]))

def merge(left, right):
	result = []
	l = 0
	r = 0
	while l < len(left):
		if r < len(right) and right[r] < left[l]:
			result.append(right[r])
			r+=1
		else:
			result.append(left[l])
			l+=1
	while r < len(right):
		result.append(right[r])
		r+=1
	return result

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
	assert sort([6,1,3,5,7,2]) == [1,2,3,5,6,7]