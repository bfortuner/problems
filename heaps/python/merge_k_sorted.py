from Heap import Heap

class MinMergeHeap(Heap):
    def __init__(self):
        Heap.__init__(self, "MIN_MERGE_HEAP")

    def get_min(self):
        return self.get_top()

    def delete_min(self):
        return self.delete(1)

    def compare_to(self, a, b):
        return a[0] < b[0]

def build_merge_heap(arr):
    heap = MinMergeHeap()
    for i in range(len(arr)):
        heap.insert([arr[i],i])
    return heap

def merge_k_sorted(lists):
    heap = MinMergeHeap()
    
    # Add first element from each
    # list To Min Heap
    for k in range(len(lists)):
        if len(lists[k]) > 0:
            val = lists[k][0]
            pos_in_k = 0
            elem = [val,k,pos_in_k]
            heap.insert(elem)

    result = []
    while heap.size > 0:
        next = heap.delete_min()
        val = next[0]
        k = next[1]
        pos_in_k = next[2]
        result.append(val)
        if pos_in_k+1 < len(lists[k]):
            new_pos_in_k = pos_in_k+1
            new_val = lists[k][new_pos_in_k]
            heap.insert([new_val,k,new_pos_in_k])
    return result



##Tests

h1 = build_merge_heap([0, 9, 5, 6, 2, 3])
assert h1.delete_min() == [0,0]
assert h1.delete_min() == [2,4]
assert h1.delete_min() == [3,5]


A = [1,3,5]
B = [2,4,6]
C = [0,3]
arrs = [A,B,C]
print merge_k_sorted(arrs)


