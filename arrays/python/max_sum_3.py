
"""
MaxSum3Array

Given array of integers, return max sum of 3 element subset

Approaches
1) Sort and return last 3 elems (n log n)
2) Nested loop (n^3)
"""

def max_sum_3_sort(arr):
	arr = sorted(arr)
	return sum(arr[len(arr)-3:])

def max_sum_3_loops(arr):
	if len(arr) < 3:
		raise Exception("Array size less than 3!")
	max_sum = sum(arr[:3])
	for i in range(len(arr)-2):
		for j in range(i+1, len(arr)-1):
			for k in range(j+1, len(arr)):
				cur_sum = arr[i] + arr[j] + arr[k]
				max_sum = max(cur_sum, max_sum)
	return max_sum

def max_sum_3_linear(arr):
	max_elems = sorted(arr[:3])
	for num in arr[3:]:
		if num > max_elems[0]:
			max_elems[0] = num
		elif num > max_elems[1]:
			max_elems[1] = num
		elif num > max_elems[2]:
			max_elems[2] = num
	return sum(max_elems)




#Tests

a1 = [1,4,3,2]
a2 = [-9,1,7,3,3,9]
a3 = [1,3]

def test_max_sum_3_sort():
	assert max_sum_3_sort(a1) == 9
	assert max_sum_3_sort(a2) == 19

def test_max_sum_3_loops():
	assert max_sum_3_loops(a1) == 9
	assert max_sum_3_loops(a2) == 19

def test_max_sum_3_linear():
	assert max_sum_3_linear(a1) == 9
	assert max_sum_3_linear(a2) == 19

if __name__ == "__main__":
	test_max_sum_3_sort()
	test_max_sum_3_loops()
	test_max_sum_3_linear()