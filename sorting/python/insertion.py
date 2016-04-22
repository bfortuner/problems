
"""
Insertion Sort

Loop Through Elements in Array "Shifting" or
Swapping that element with its element on the left
until that element is sorted. This creates a 
sorted left sub array. Continue until end of
array 

Worst Case: O(n^2)
Best Case: O(n^2)
"""


def sort(arr):
	for i in range(len(arr)):
		j = i
		while j > 0:
			cur_val = arr[j]
			if cur_val < arr[j-1]:
				arr[j] = arr[j-1]
				arr[j-1] = cur_val
			else:
				break
			j-=1
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