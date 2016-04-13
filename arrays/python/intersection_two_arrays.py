"""
[Intersection Two Arrays]

Given two unsorted integer arrays, return a 3rd array with 
the intersection (distinct elements that appear in both arrays). 
Optimize for time and space complexity.

a1 = [1,6,3,7]
a2 = [3,4,7]
res = [3,7]

Cases
1) No overlapping elements
2) Empty arrays
3) Arrays of different lengths
4) Duplicate elements in array 1 or 2


Approaches
1) Loop through a1, loop through result to avoid dupes, if also in a2, add to result 
O(n^2)
2) Sort both arrays (n log n). Iterate through together. If elems equal. Add to result set. Continue until
non-equal values found in each array or end reached. If not equal, increment lesser value. Continue until
both pointers at end of respective arrays 
O(n + m + (n log n)) + O(1) space
3) HashSet or Set. Loop through a1 and add to Set. Loop through a2, if value in Set add value to Result array.
O(n + m) + O(n) space
4)
"""

"""
1,4,6,7
2,2,4,7

Python Set()
So basically a set uses a hashtable as it's underlying data structure, but just stores keys
This explains the O(1) membership checking, since looking up an item in a 
hashtable is an O(1) operation, on average.

"""

# O(n + m) time, O(n) space
def intersection_1(a1, a2):
	distincts_in_a1 = set()
	for elem in a1:
		if elem not in distincts_in_a1:
			distincts_in_a1.add(elem)
	intersection_of_a1_a2 = []
	for elem in a2:
		if elem in distincts_in_a1:
			intersection_of_a1_a2.append(elem)
	return intersection_of_a1_a2

# O(n log n + n) time, O(intersection) space
def intersection_2(arr1, arr2):
	arr1 = sorted(arr1)
	arr2 = sorted(arr2)
	a = 0
	b = 0
	result = []
	while a < len(arr1) and b < len(arr2):
		a_val = arr1[a]
		b_val = arr2[b]
		if a_val == b_val: 
			# we found an intersection, add to result and
			# increment  until next non-equal value found
			result.append(a_val)
			while a < len(arr1) and arr1[a] == a_val:
				a += 1
			while b < len(arr2) and arr2[b] == b_val:
				b += 1
		elif a_val < b_val:
			a += 1
		else:
			b += 1
	return result




#Tests

a1 = [1,4,6,7,1]
a2 = [2,2,4,7,-5]
a3 = []
a4 = [2]
a5 = [1,6,3,7]
a6 = [4,3,7]

def test_intersection_1():
	assert intersection_1(a1, a2) == [4,7]
	assert intersection_1(a1, a3) == []
	assert intersection_1(a2, a4) == [2]
	assert intersection_1(a5, a6) == [3,7]

def test_intersection_2():
	assert intersection_2(a1, a2) == [4,7]
	assert intersection_2(a1, a3) == []
	assert intersection_2(a2, a4) == [2]
	assert intersection_2(a5, a6) == [3,7]

if __name__ == "__main__":
	test_intersection_1()
	test_intersection_2()



