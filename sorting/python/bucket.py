
"""
Bucket Sort

Given list of n numeric inputs between 0 and some maximum value M, 
divide the value range into n buckets each of size M/n. 
It stores a LinkedList in each bucket and uses insertion sort to keep 
the LinkedList sorted if multiple values map to the same bucket.

Average Case - O(n+k)  - k is the range of values and n is the number of values
Worst Case - O(n^2) - when all values map to the same bucket 
(i.e. you have to do an insertion sort on the same bucket)
"""

class Node(object):
	def __init__(self, val, next_node=None):
		self.val = val
		self.next = next_node
"""
arr = [10,2,9,7,1] #be careful if you are including 0 or not! 
					with 0 you have 11 numbers and bucket size is 11/5
bks = [N,N,N,N,N] 
max_value = 10
num_buckets = 5
bucket_size = 2.2
"""

def sort(arr):
	max_value = max(arr)
	num_buckets = len(arr) # create bucket array of size N #4
	bucket_size = (max_value+1) / float(num_buckets) #+1 to account for 0
	buckets = [None for x in range(num_buckets)]
	for num in arr:
		index = int(num / bucket_size)
		#insert into bucket - we fill up buckets with nodes
		buckets = insert_elem_into_buckets(num, index, buckets)
	#we loop through buckets, if not None
	#While not None, we pop value of Node back onto arr
	arr_index = 0
	for bucket in buckets:
		if bucket is not None:
			node = bucket
			while node is not None:
				arr[arr_index] = node.val
				arr_index+=1
				node = node.next
	return arr

def insert_elem_into_buckets(num, index, buckets):
	if buckets[index] is None:
		buckets[index] = Node(num)
		return buckets
	new_node = Node(num)
	cur_node = buckets[index]
	if new_node.val <= cur_node.val:
		new_node.next = cur_node
		buckets[index] = new_node
		return buckets
	prior_node = cur_node
	while cur_node.next is not None \
		and cur_node.val < new_node.val:
		prior_node = cur_node
		cur_node = cur_node.next
	# we have gotten to the end
	if cur_node.next is None:
		cur_node.next = new_node
	# we are still in the middle
	else:
		prior_node.next = new_node
		new_node.next = cur_node
	return buckets

if __name__ == "__main__":
	assert sort([1,10,5]) == [1,5,10]
	assert sort([3,2,5,5]) == [2,3,5,5]
	assert sort([3,2,5]) == [2,3,5]
	assert sort([2,1]) == [1,2]
	assert sort([1,2]) == [1,2]
	assert sort([1]) == [1]
	assert sort([1,2,3,4]) == [1,2,3,4]
	assert sort([2,3,5,2,5,5]) == [2,2,3,5,5,5]
	assert sort([2,3,5,0,5,5]) == [0,2,3,5,5,5]
	assert sort([6,1,3,5,7,2]) == [1,2,3,5,6,7]