from Heap import MaxHeap
from test_data import *

"""
Delete the ith element in a MaxHeap
given only access to the methods
get_left, get_right, get_parent
and delete(i)

Basically you can't go straight to i,
You have to use the get left and right
operations 
"""

def delete_ith(heap, i):
    print "INPUT: " + str(heap.heap)
    path_to_i = []
    i = i//2
    while i > 0:
        path_to_i.insert(0,i)
        i = i//2

    elem = None
    for i in path_to_i:
        if i % 2 == 0:
            elem = heap.get_left(i)
        else:
            elem = heap.get_right(i)
    heap.delete(elem)
    print "OUTPUT: " + str(heap.heap)
    return heap

heap = delete_ith(mx_hp, 4)
 
