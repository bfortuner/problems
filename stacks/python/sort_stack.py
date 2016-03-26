from Stack import Stack
from Stack import build_stack_from_list

"""
Sort Stack

Write a method to sort a stack in ascending order using Push, Pop, Peek, and IsEmpty.

Approach: 3 stacks
1) Can I come up with a more efficient solution?

"""


def sort_stack(stack):
	large = Stack()
	small = Stack()
	while not stack.is_empty() or not small.is_empty():
		while not stack.is_empty():
			value = stack.pop()
			if large.is_empty() or small.is_empty():
				if stack.peek() is None:
					large.push(value)
				elif value > stack.peek():
					large.push(value)
					small.push(stack.pop())
				else:
					large.push(stack.pop())
					small.push(value)
			elif value > large.peek():
				small.push(large.pop())
				large.push(value)
			else:
				small.push(value)
		tmp = stack
		stack = small
		small = tmp
	return large



#Tests

def test_sort_stack():
	inputstack = build_stack_from_list([3,4,1])
	outputstack = sort_stack(inputstack)

	answerstack = build_stack_from_list([4,3,1])
	assert answerstack.equals(outputstack) == True

def test_sort_stack_big():
	inputstack = build_stack_from_list([3,6,2,9,10,4,1])
	outputstack = sort_stack(inputstack)
	outputstack.display()

	answerstack = build_stack_from_list([10,9,6,4,3,2,1])
	assert answerstack.equals(outputstack) == True

def test_sort_stack_1_element():
	inputstack = build_stack_from_list([3])
	outputstack = sort_stack(inputstack)

	answerstack = build_stack_from_list([3])
	assert answerstack.equals(outputstack) == True

def test_sort_stack_empty():
	inputstack = build_stack_from_list([])
	outputstack = sort_stack(inputstack)

	answerstack = build_stack_from_list([])
	assert answerstack.equals(outputstack) == True

if __name__ == "__main__":
	test_sort_stack()
	test_sort_stack_1_element()
	test_sort_stack_empty()
	test_sort_stack_big()
