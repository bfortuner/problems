from Node import Node
from LinkedList import *

"""
Merge two sorted LinkedLists
given pointer to each list's head node
"""
def merge_sorted_linked_lists(left, right):
    before_head = Node(None)
    cur = before_head
    while left != None and right != None:
        if left.value <= right.value:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    if left != None:
        cur.next = left
    else:
        cur.next = right
    return before_head.next



# Tests

def test_merge_sorted_linked_lists():
    llA = build_ll_from_lst([1,3,5])
    llB = build_ll_from_lst([2,4])
    headA = llA.head
    headB = llB.head

    mergedList = LinkedList(merge_sorted_linked_lists(headA, headB))
    answerList = build_ll_from_lst([1,2,3,4,5])
    assert answerList.lists_eq(mergedList)

    llC = build_ll_from_lst([1,4,5])
    llD = build_ll_from_lst([2,3])
    headC = llC.head
    headD = llD.head

    mergedList2 = LinkedList(merge_sorted_linked_lists(headC, headD))
    answerList2 = build_ll_from_lst([1,2,3,4,5])
    assert answerList2.lists_eq(mergedList2)

    #List A is None
    llA = build_ll_from_lst([])
    llB = build_ll_from_lst([2,4])
    headA = llA.head
    headB = llB.head

    mergedList = LinkedList(merge_sorted_linked_lists(headA, headB))
    answerList = build_ll_from_lst([2,4])
    assert answerList.lists_eq(mergedList)

    #List B is longer
    llA = build_ll_from_lst([2,4])
    llB = build_ll_from_lst([2,3,5])
    headA = llA.head
    headB = llB.head

    mergedList = LinkedList(merge_sorted_linked_lists(headA, headB))
    answerList = build_ll_from_lst([2,2,3,4,5])
    assert answerList.lists_eq(mergedList)

    
if __name__ == "__main__":
    test_merge_sorted_linked_lists()
  
  
  
  
  
  
