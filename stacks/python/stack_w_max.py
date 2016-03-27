from Stack import Stack
from Node import Node
import sys

"""
Stack w Max

Create a data structure that efficiently supports the stack operations 
(push and pop) and also a return-the-maximum operation. Assume the 
elements are real numbers so that you can compare them.

Approaches
1) Before Push(), check if value > max, and set max. After Pop(), loop through Linked List and find new max.
2) ???

"""

class StackWithMax(Stack):
	def __init__(self, head=None):
		super(StackWithMax, self).__init__(head)
		self.max = self.get_max()

	def get_max(self):
		cur_max = None
		cur_node = self.head
		while cur_node is not None:
			if cur_max is None or cur_node.value > cur_max:
				cur_max = cur_node.value
			cur_node = cur_node.next
		return cur_max

	def push(self, value):
		if value > self.max:
			self.max = value
		super(StackWithMax, self).push(value)

	def pop(self):
		value = super(StackWithMax, self).pop()
		self.max = self.get_max()
		return value



#Tests

def build_stack_from_list(lst):
	stack = StackWithMax()
	for val in lst:
		stack.push(val)
	return stack

def test_basic_ops():
	stack = StackWithMax()
	test_values = [1,2,3]
	for val in test_values:
		stack.push(val)
	assert stack.size() == 3

	answer_values = [3,2,1]
	for val in answer_values:
		assert stack.pop() == val
	assert stack.size() == 0

def test_get_max():
	inputstack = build_stack_from_list([3,4,1])
	inputstack.display()
	assert inputstack.get_max() == 4
	inputstack.pop()
	assert inputstack.get_max() == 4
	inputstack.pop()
	assert inputstack.get_max() == 3
	inputstack.pop()
	assert inputstack.get_max() == None

def test_get_max_big():
	inputstack = build_stack_from_list([3,6,2,9,10,4,1,-4,6])
	assert inputstack.get_max() == 10

def test_get_max_1_element():
	inputstack = build_stack_from_list([3])
	assert inputstack.get_max() == 3

	assert inputstack.pop() == 3
	assert inputstack.get_max() == None

def test_get_max_empty():
	inputstack = build_stack_from_list([])
	assert inputstack.get_max() == None


if __name__ == "__main__":
	test_basic_ops()
	test_get_max()
	test_get_max_1_element()
	test_get_max_empty()
