
"""
Selection Sort

Loop Through Array finding smallest 
element and swap with current element.
Move to next element and continue. 

Worst Case: O(n^2)
Best Case: O(n^2)
"""

def sort(arr):
	for i in range(len(arr)):
		cur_val = arr[i]
		smallest = None
		for j in range(i+1, len(arr)):
			if smallest is None or arr[j] < arr[smallest]:
				smallest = j
		if smallest is not None and arr[smallest] < cur_val:
			arr[i] = arr[smallest]
			arr[smallest] = cur_val
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