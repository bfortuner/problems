from LinkedList import LinkedList
from Node import Node
from LinkedList import build_ll_from_lst 

"""
Merge Sort Linked List
"""

def sort(head):
    if head == None:
        return None
    if head.next == None:
        return head    
    mid = get_middle_node(head)
    left = sort(head)
    right = sort(mid)
    return merge(left, right)
    
def merge(left, right):
    before_head = Node(None)
    cur = before_head
    while left != None:
        if right == None or left.value <= right.value:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    while right != None:
        cur.next = right
        right = right.next
        cur = cur.next
    return before_head.next

def get_middle_node(head):
    before_slow = head
    slow = head
    fast = head
    while fast != None:
        fast = fast.next
        if fast != None:
            before_slow = slow
            fast = fast.next
            slow = slow.next
    before_slow.next = None
    return slow
        


## Test Get Middle Node
t0 = build_ll_from_lst([5,3,6,2])
print get_middle_node(t0.head).value == 6


## Test Merge
t1 = build_ll_from_lst([1,3,4,6]).head
t2 = build_ll_from_lst([2,3,5]).head
print LinkedList(merge(t1,t2)).get_linked_list_str()

## Test Sort
t4 = build_ll_from_lst([5,3,6,2,14,7,2,3])
t5 = build_ll_from_lst([3,2,1])
t6 = build_ll_from_lst([3,2,2,3])
t7 = build_ll_from_lst([1])
t8 = build_ll_from_lst([4,2,3,1,6,3,2])
print LinkedList(sort(t4.head)).get_linked_list_str()
print LinkedList(sort(t5.head)).get_linked_list_str()
print LinkedList(sort(t6.head)).get_linked_list_str()
print LinkedList(sort(t7.head)).get_linked_list_str()
print LinkedList(sort(t8.head)).get_linked_list_str()
