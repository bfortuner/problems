
"""
Sort 012

Sort an array that contains only the integers 
0, 1, and 2 in linear time. 

(e.g. [1,0,2,2,1] == [0,1,1,2,2])

O(n)
"""

def sort(arr):
	count_arr = [0 for x in range(3)]
	for num in arr:
		count_arr[num] += 1
	count_index = 0
	for i in range(len(arr)):
		if count_arr[count_index] == 0:
			count_index += 1
		arr[i] = count_index
		count_arr[count_index] -= 1
	return arr

if __name__ == "__main__":
	assert sort([1,2,1,0,1,2]) == [0,1,1,1,2,2]
	assert sort([2,1]) == [1,2]
	assert sort([1,2]) == [1,2]
	assert sort([1]) == [1]
