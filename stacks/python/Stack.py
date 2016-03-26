from Node import Node

"""
Implement Stack - Push and Pop methods

Assumptions:
1) Stack cannot handle None values

"""

class Stack(object):

	def __init__(self, head=None):
		self.head = head

	def push(self, value):
		"""
		Add value to top of Stack
		"""
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		"""
		Return and remove value
		on top of Stack
		"""
		if self.head is None:
			return None
		value = self.head.value
		self.head = self.head.next
		return value

	def display(self):
		node = self.head
		while node is not None:
			print "   " + str(node.value)
			node = node.next
		print "-------"

	def size(self):
		count = 0
		node = self.head
		while node is not None:
			count += 1
			node = node.next
		return count



# Tests

def test_basic_ops():
	stack = Stack()
	test_values = [1,2,3]
	for val in test_values:
		stack.push(val)
		stack.display()
	assert stack.size() == 3

	answer_values = [3,2,1]
	for val in answer_values:
		assert stack.pop() == val
		stack.display()
	assert stack.size() == 0

def test_size():
	stack = Stack()
	assert stack.size() == 0
	stack.push("A")
	assert stack.size() == 1
	stack.push("B") 
	assert stack.size() == 2
	stack.pop()
	assert stack.size() == 1
	stack.pop()
	assert stack.size() == 0
	stack.pop()
	assert stack.size() == 0

def build_stack_from_list(lst):
	stack = Stack()
	for val in lst:
		stack.push(val)
	return stack

	

if __name__ == "__main__":
	test_basic_ops()
	test_size()
