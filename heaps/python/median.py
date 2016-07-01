from Heap import MinHeap, MaxHeap

"""
Approaches for Median:

1) Buckets from MIN to MAX value
increment count in each bucket 
store total count of elements
loop through until you reach total/2
2) Sort array and return middle value
3) Balanced Binary Tree (in order traversal
produces a sorted list in O(n) time
you can stop once you reach n/2 nodes)
4) Infinite Stream?
You could use a HashMap to store the 
count of duplicate values found
if you are deleteMin, first check
HashMap and decrement if > 1
"""

class MedianHeap(object):

    def __init__(self):
        self.minheap = MinHeap()
        self.maxheap = MaxHeap()

    def get_median(self):
        if self.minheap.size == self.maxheap.size:
            return (self.minheap.get_min() + self.maxheap.get_max()) / 2.0
        elif self.minheap.size > self.maxheap.size:
            return self.minheap.get_min()
        else:
            return self.maxheap.get_max()

    def insert(self, value):
        if self.minheap.size == 0:
            self.minheap.insert(value)
        elif value > self.minheap.get_min():
            self.minheap.insert(value)
        else:
            self.maxheap.insert(value)
        self.rebalance()
        
    def rebalance(self):
        if self.minheap.size < self.maxheap.size-1:
            self.minheap.insert(self.maxheap.delete_max())
        elif self.maxheap.size < self.minheap.size-1:
            self.maxheap.insert(self.minheap.delete_min())
            

def get_median_of_arr(arr):
    if arr is None or len(arr) < 1:
        return None
    arr.sort()
    if len(arr) % 2 == 1:
        return arr[len(arr)/2]
    else:
        left = len(arr)/2 - 1
        right = len(arr)/2
        return (arr[left]+arr[right])/2.0

## Tests

input = [-10,5,0,3,6,1]
medianheap = MedianHeap()
for val in input:
    medianheap.insert(val)

assert get_median_of_arr(input) == 2.0
assert medianheap.get_median() == 2.0

input2 = [1,2,3,4,5,6,7]
m2 = MedianHeap()
for val in input2:
    m2.insert(val)
assert m2.get_median() == 4
assert get_median_of_arr(input2) == 4
