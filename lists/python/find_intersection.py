from LinkedList import LinkedList
from LinkedList import build_ll_from_lst
from Node import Node

"""
Given pointers to the head nodes of 2 linked lists that merge 
together at some point, find the Node where the two lists merge.

Assumptions:
1) Head nodes will not be NULL
2) Lists will always merge at some point

Approaches:
1) Hashmap + 2 loops - Loop through first LL and add all object hash ids + value
to hashmap. Loop through second and check if ID is in hashmap. Return value associated
with first node found (since that would be first intersection)
2) O(1) space, but O(n^2) time? For each node in L1, loop through L2 and until NULL and check
for intersection. Keep going until first intersection is found. Average case not terrible...
3) Linear time? Recursive?

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

 1
  \
   2--->3--->NULL
  /
 1
#Returns 2

1--->2
      \
       3--->Null
      /
     1
#Returns 3

"""

def find_intersection_hashmap(headA, headB):
	hashmap = {}
	while headA is not None:
		hashmap[id(headA)] = headA.value
		headA = headA.next

	while headB is not None:
		hash_id = id(headB)
		if hashmap.get(hash_id) is not None:
			return hashmap[hash_id]
		headB = headB.next
	return None



#Tests

def test_find_intersection_hashmap():
	fourth_node = Node("D")
	third_node = Node("C", fourth_node)
	second_node = Node("B", third_node)
	head1 = Node("A", second_node)

	second_node2 = Node("B2", third_node)
	head2 = Node("A2", second_node2)

	assert find_intersection_hashmap(head1, head2) == "C"



if __name__ == "__main__":
	test_find_intersection_hashmap()

