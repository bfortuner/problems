from Node import Node
from DoublyNode import DoublyNode

class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def set_head(self, new_head):
		self.head = new_head

	def get_head(self):
		return self.head

	def get_linked_list_str(self):
		linked_list_str = ""
		cur_node = self.head
		while cur_node is not None:
			linked_list_str = linked_list_str + str(cur_node.value) + "->"
			cur_node = cur_node.get_next()
		return linked_list_str

	def remove_last_node(self):
		node = self.head
		if node.get_next() == None:
			return
		while node.get_next().get_next() is not None:
			node = node.get_next()
		node.set_next(None)

	def lists_eq(self, other_list):
		'''
		Python by default checks if 
		two objects exist in same memory space
		'''
		if other_list == self:
			return True
		if not isinstance(other_list, LinkedList):
			return False
		node = self.head
		other_node = other_list.head
		while node is not None:
			if other_node is None:
				return False
			elif other_node.value != node.value:
				return False
			node = node.get_next()
			other_node = other_node.get_next()
		return other_node is None

	def get_size(self):
		size = 0
		node = self.head
		while node is not None:
			size += 1
			node = node.get_next()
		return size

	def contains_value(self, value):
		node = self.head
		while node is not None:
			if node.value == value:
				return True
			node = node.get_next()
		return False

	def remove_cur_node(self, node):
		if node == None:
			return
		while node.get_next() != None:
			prior_node = node
			next = node.get_next()
			node.set_value(next.value)
			node = next
		prior_node.set_next(None)

	def remove_node_after_cur_node(self, node):
		if node == None or node.get_next() == None:
			return
		node.set_next(node.get_next().get_next())

	def insert_after_node(self, node, new_node):
		new_node.set_next(node.get_next())
		node.set_next(new_node)

	def remove_node_by_value(self, val):
		node = self.head
		if node == None:
			return
		while node != None and node.value != val:
			prior_node = node
			node = node.get_next()
		if node != None:
			prior_node.set_next(node.get_next())

	def append(self, val):
		"""
		Add value to end of list
		"""
		if self.head is None:
			self.head = Node(val)
			return
		cur_node = self.head
		while cur_node.next is not None:
			cur_node = cur_node.next
		cur_node.next = Node(val)



# Tests

def test_remove_node_by_value():
	l1 = build_ll_from_lst(["A","B","C"])
	l1.remove_node_by_value("B")

	a1 = build_ll_from_lst(["A","C"])
	assert l1.lists_eq(a1)

def test_insert_after_node():
	l1 = build_ll_from_lst(["A","C"])
	node = l1.head
	l1.insert_after_node(node,Node("B"))

	a1 = build_ll_from_lst(["A","B","C"])
	assert l1.lists_eq(a1)

def test_remove_node_after_cur_node():
	l4 = build_ll_from_lst(["A","B","C"])
	node = l4.head.get_next()
	l4.remove_node_after_cur_node(node)

	a4 = build_ll_from_lst(["A","B"])
	assert l4.lists_eq(a4)

def test_remove_cur_node():
	l4 = build_ll_from_lst(["A","B","C"])
	node = l4.head.get_next()
	l4.remove_cur_node(node)

	a4 = build_ll_from_lst(["A","C"])
	assert l4.lists_eq(a4)

def test_build_ll_from_lst():
	lst1 = []
	lst2 = ["A"]
	lst3 = ["A","B"]

	ll1 = LinkedList()
	ll2 = LinkedList(Node("A"))
	ll3 = LinkedList(Node("A"))
	ll3.head.set_next(Node("B"))

	assert ll1.lists_eq(build_ll_from_lst(lst1))
	assert ll2.lists_eq(build_ll_from_lst(lst2))
	assert ll3.lists_eq(build_ll_from_lst(lst3))

def test_contains_value():
	l1 = build_ll_from_lst([])
	l2 = build_ll_from_lst(["A"])
	l3 = build_ll_from_lst(["A","B"])

	assert l1.contains_value("A") == False
	assert l2.contains_value("A") == True
	assert l2.contains_value("B") == False
	assert l3.contains_value("B") == True
	assert l3.contains_value("C") == False

def test_get_size():
	test_list = get_test_linked_list()
	assert test_list.get_size() == 3

	empty_list = LinkedList()
	assert empty_list.get_size() == 0

def test_remove_last_node():
	#A -- > B -- > C --> None
	#A -- > B -- > None
	test_list = get_test_linked_list()
	second_node = Node("B")
	head = Node("A", second_node)
	answer_list = LinkedList(head)

	test_list.remove_last_node()
	assert(test_list.lists_eq(answer_list))

def test_lists_eq__same_object():
	node = Node("A")
	test_list = LinkedList(node)
	test_list_cp = test_list
	assert test_list.lists_eq(test_list_cp)
	assert test_list.lists_eq(test_list)

def test_lists_eq__other_not_instance_of_linked_list():
	node = Node("A")
	test_list = LinkedList(node)
	not_linked_list = "ABC"
	assert not test_list.lists_eq(not_linked_list)

def test_lists_eq__one_node():
	node = Node("A")
	test_list = LinkedList(node)
	other_list = LinkedList(node)
	assert test_list.lists_eq(other_list)

	other_node = Node("A")
	other_list2 = LinkedList(other_node)
	assert test_list.lists_eq(other_list2)

def test_lists_eq__lists_empty():
	test_list = LinkedList()
	other_list = LinkedList()
	assert test_list.lists_eq(other_list)

	node = Node("A")
	test_list.set_head(node)
	assert not test_list.lists_eq(other_list)
	assert not other_list.lists_eq(test_list)

def test_build_linked_list():
	test_list = get_test_linked_list()
	new_head = Node("Z")
	new_head.set_next(test_list.head)
	test_list.set_head(new_head)

	cur_node = test_list.head
	assert cur_node.value == "Z"

	cur_node = cur_node.get_next()
	assert cur_node.value == "A"

	cur_node = cur_node.get_next()
	assert cur_node.value == "B"

	cur_node = cur_node.get_next()
	assert cur_node.value == "C"

	cur_node = cur_node.get_next()
	assert cur_node is None

def test_get_linked_list_str():
	test_list = get_test_linked_list()
	list_str = test_list.get_linked_list_str()
	assert list_str == "A->B->C->"

def test_append():
	inputlist = build_ll_from_lst([1,2,3])
	answerlist = build_ll_from_lst([1,2,3,4])
	inputlist.append(4)
	assert answerlist.lists_eq(inputlist)

	inputlist = build_ll_from_lst([])
	answerlist = build_ll_from_lst([4])
	inputlist.append(4)
	assert answerlist.lists_eq(inputlist)



## Helpers

def build_ll_from_lst(lst):
	ll = LinkedList()
	if len(lst) == 0:
		return ll
	ll.set_head(Node(lst[0]))
	node = ll.head
	i = 1
	while i < len(lst):
		new_node = Node(lst[i])
		node.set_next(new_node)
		node = new_node
		i += 1
	return ll

def build_doubly_ll_from_lst(lst):
	ll = LinkedList()
	if len(lst) == 0:
		return ll
	ll.set_head(DoublyNode(lst[0]))
	node = ll.head
	i = 1
	while i < len(lst):
		new_node = DoublyNode(lst[i])
		new_node.prev = node
		node.next = new_node
		node = new_node
		i += 1
	return ll

def get_test_linked_list():
	third_node = Node("C")
	second_node = Node("B", third_node)
	head = Node("A", second_node)

	test_list = LinkedList(head)
	return test_list


if __name__ == "__main__":
	#Run all Tests
	print "LinkedList tests starting!"
	test_build_linked_list()
	test_get_linked_list_str()
	test_remove_last_node()
	test_lists_eq__same_object()
	test_lists_eq__other_not_instance_of_linked_list()
	test_lists_eq__one_node()
	test_lists_eq__lists_empty()
	test_get_size()
	test_build_ll_from_lst()
	test_contains_value()
	test_remove_cur_node()
	test_remove_node_after_cur_node()
	test_insert_after_node()
	test_remove_node_by_value()
	test_append()
	print "LinkedList tests complete!"