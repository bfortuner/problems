
"""
Shell Sort

Insertion Sort, but with a diminishing increment (i = 3),
sometimes called the gap, used to create a sublist by choosing 
all items that are i items apart. Sorts those sublists using 
insertion sort, and then completes one final normal insertion
(increment = 1) sort at the end

Average Case - O(n^2)
Worst Case - O(n^2)
"""
DEFAULT_HOP = 1

def sort(arr, hop=DEFAULT_HOP):
	i = 0
	while i < hop:
		arr = insertion_sort_w_hop(arr, i, hop)
		i+=1
	arr = insertion_sort_w_hop(arr, 0, 1)
	return arr

def insertion_sort_w_hop(arr, start, hop):
	i = start
	while i < len(arr):
		j = i
		while j-hop >= 0 and arr[j] < arr[j-hop]:
			cur = arr[j]
			arr[j] = arr[j-hop]
			arr[j-hop] = cur
			j -= hop
		i += hop
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
	assert sort([6,1,3,5,7,2]) == [1,2,3,5,6,7]