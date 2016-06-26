from abc import ABCMeta
from abc import abstractmethod

class Heap(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, heapType):
        #first element is placeholder to make integer math work
        self.heap = [None] 
        self.size = 0
        self.heapType = heapType

    def get_parent(self, i):
        return i // 2 #python floor division (python 2.7 this is default)

    def get_left(self, i):
        return i*2

    def get_right(self, i):
        return i*2 + 1

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.perc_up(self.size)

    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    def perc_up(self, i):
        while i > 1:
            parent = self.get_parent(i)
            if self.compare_to(self.heap[i],self.heap[parent]):
                self.swap(i, parent)
            i = parent

    def perc_down(self, i):
        while self.get_left(i) <= self.size:
            mc = self.get_foremost_child(i)
            if self.compare_to(self.heap[mc],self.heap[i]):
                self.swap(i, mc)
            i = mc

    def get_top(self):
        """Get max or min element depending on heap type"""
        if self.size == 0:
            return -1
        return self.heap[1]

    def delete(self, i):
        """Delete max or min element depending on heap type"""
        if self.size == 0:
            return
        return_val = self.heap[i]
        self.heap[i] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.perc_down(i)
        return return_val
    
    def get_foremost_child(self, i):
        """Get max or min child depending on HeapType"""
        lc = self.get_left(i)
        rc = self.get_right(i)
        if rc > self.size or self.compare_to(self.heap[lc],self.heap[rc]):
            return lc
        return rc

    @abstractmethod
    def compare_to(self, a, b):
        """Must be overridden by children"""
        return


class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self, "MAX_HEAP")

    def get_max(self):
        return self.get_top()
    
    def delete_max(self):
        self.delete(1)
        
    def compare_to(self, a, b):
        return a > b


class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self, "MIN_HEAP")

    def get_min(self):
        return self.get_top()

    def delete_min(self):
        self.delete(1)

    def compare_to(self, a, b):
        return a < b



"""
Build Heap From Unsorted Array
interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
Complexity O(n)
"""

def build_heap(arr, heapType):
    if heapType == "MAX_HEAP":
        new_heap = MaxHeap()
    else:
        new_heap = MinHeap()
    new_heap.size = len(arr)
    new_heap.heap = [0] + arr
    i = len(arr) // 2
    while i > 0:
        new_heap.perc_down(i)
        i-=1
    return new_heap
        


## Tests

if __name__ == "__main__":
    mx_hp = build_heap([0, 9, 5, 6, 2, 3],"MAX_HEAP")
    print mx_hp.heap
    assert mx_hp.get_max() == 9
    mx_hp.delete_max()
    assert mx_hp.get_max() == 6

    mn_hp = build_heap([0, 9, 5, 6, 2, 3],"MIN_HEAP")
    print mn_hp.heap
    assert mn_hp.get_min() == 0
    mn_hp.delete_min()
    assert mn_hp.get_min() == 2




    assert issubclass(MaxHeap, Heap)
    assert isinstance(MaxHeap(), Heap)


    ##MAX HEAP
    max_heap = MaxHeap()
    max_heap.insert(1)
    max_heap.insert(5)
    max_heap.insert(8)
    max_heap.insert(3)
    max_heap.insert(15)

    assert max_heap.get_max() == 15
    assert max_heap.size == 5
    max_heap.delete_max()

    max_heap.insert(9)
    assert max_heap.get_max() == 9
    assert max_heap.size == 5

    max_heap.delete_max()
    assert max_heap.get_max() == 8
    assert max_heap.size == 4

    max_heap.delete_max()
    assert max_heap.get_max() == 5
    assert max_heap.size == 3

    max_heap.delete_max()
    assert max_heap.get_max() == 3
    assert max_heap.size == 2

    max_heap.delete_max()
    assert max_heap.get_max() == 1
    assert max_heap.size == 1


    ##MIN HEAP
    min_heap = MinHeap()
    min_heap.insert(1)
    min_heap.insert(5)
    min_heap.insert(8)
    min_heap.insert(3)
    min_heap.insert(15)

    assert min_heap.get_min() == 1
    assert min_heap.size == 5
    min_heap.delete_min()

    min_heap.insert(9)
    assert min_heap.get_min() == 3
    assert min_heap.size == 5

    min_heap.delete_min()
    assert min_heap.get_min() == 5
    assert min_heap.size == 4

    min_heap.delete_min()
    assert min_heap.get_min() == 8
    assert min_heap.size == 3

    min_heap.delete_min()
    assert min_heap.get_min() == 9
    assert min_heap.size == 2

    min_heap.delete_min()
    assert min_heap.get_min() == 15
    assert min_heap.size == 1
