"""
Heapsort
O(nlogn) time
O(1) space - constant space

Steps:
1) Build Heap (in-place) - O(n)
2) Swap Max Element To End, then Heapify Array - O(logn)
3) Repeat O(n)

Heap sort algorithm has limited uses because 
Quicksort and Mergesort are better in practice.

https://en.wikipedia.org/wiki/Heapsort#Comparison_with_other_sorts

However, heapsort is nice b/c it guarantees O(nlogn) 
and uses O(1) constant space
"""


def sort(arr):
    """Sort in ASC order using MAX Heap"""
    size = len(arr)

    ##Step 1 - Heapify Array in-place
    arr = build_heap(arr)

    ##Step 2 - Swap Max Element To End, then Heapify
    while size > 0:
        swap(arr,1,size)
        size-=1
        perc_down(arr,1,size)
    return arr[1:]

def build_heap(arr):
    """
    Heapify Array In-Place 
    Starting From Middle b/c leaf nodes 
    always satisfy the heap propery
    """
    i = len(arr)//2
    size = len(arr)
    arr = [0] + arr
    while i > 0:
        perc_down(arr,i,size)
        i-=1
    return arr

def perc_down(arr, i, size):
    while 2*i <= size:  #left child
        mc = get_max_child(arr,i,size)
        if arr[mc] > arr[i]:
            swap(arr,mc,i)
        else: #If elements are sorted, stop
            break
        i = mc

def get_max_child(arr, i, size):
    if 2*i+1 > size:
        return 2*i
    elif arr[2*i] > arr[2*i+1]:
        return 2*i
    return 2*i+1

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


a1 = [17,2,6,1,4,5,2]
assert sort(a1) == [1,2,2,4,5,6,17]

a2 = [12,11,13,5,6,7]
assert sort(a2) == [5, 6, 7, 11, 12, 13]
