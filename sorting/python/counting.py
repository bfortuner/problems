
"""
Counting Sort

Creates a bucket array from 0 to M (max value), 
and then increments the count for each element it finds. 
It loops through the bucket array adding to it the sum of the 
previous bin, this results in a mapping of the position of 
each element in the new sorted array.

http://www.geeksforgeeks.org/counting-sort/
http://en.wikipedia.org/wiki/Counting_sort
https://www.cs.usfca.edu/~galles/visualization/CountingSort.html

Average Case - O(n)
Worst Case - O(n)
"""

def sort(arr):
	max_num = max(arr)
	count_arr = [0 for x in range(max_num+1)]
	sorted_arr = [0 for x in range(len(arr))]
	for num in arr:
		count_arr[num] += 1
	for i in range(len(count_arr)):
		if i > 0:
			count_arr[i] += count_arr[i-1]
	for num in arr:
		count_arr[num] -= 1
		pos_in_sorted = count_arr[num]
		sorted_arr[pos_in_sorted] = num
	return sorted_arr

if __name__ == "__main__":
	assert sort([3,2,5,5]) == [2,3,5,5]
	assert sort([3,2,5]) == [2,3,5]
	assert sort([2,1]) == [1,2]
	assert sort([1,2]) == [1,2]
	assert sort([1]) == [1]
	assert sort([1,2,3,4]) == [1,2,3,4]
	assert sort([1,3,1,0,3,2]) == [0,1,1,2,3,3]
	assert sort([2,3,5,2,5,5]) == [2,2,3,5,5,5]
	assert sort([2,3,5,0,5,5]) == [0,2,3,5,5,5]
	assert sort([6,1,3,5,7,2]) == [1,2,3,5,6,7]
