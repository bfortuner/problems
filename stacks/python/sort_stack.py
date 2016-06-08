from Stack import Stack
from Stack import build_stack_from_list

"""
Sort Stack

Write a method to sort a stack in ascending order

Approaches: 
1) 3 stacks - Small, Large, Current
2) Recursive - Sort and Insertion Sort
"""

def sort_stack_recursive(stack):
        if len(stack) == 0:
                return
        elem = stack.pop()
        sort_stack_recursive(stack)
        insert(stack, elem)

def insert(stack, elem):
        """Insertion Sort for Stacks!"""
        if len(stack) == 0:
                stack.append(elem)
        else:
                top = stack.pop()
                #To reverse a stack just remove this conditional
                if top >= elem:
                        stack.append(top)
                        stack.append(elem)
                else:
                        insert(stack, elem)
                        stack.append(top)
                        
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
	inputstack = build_stack_from_list([3,6,2,9,10,4,1,-4,6])
	outputstack = sort_stack(inputstack)
	outputstack.display()

	answerstack = build_stack_from_list([10,9,6,6,4,3,2,1,-4])
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

def test_sort_stack_recursive():
        s1 = [8,3,1,4,2,5,9,7,6]
        outputstack = [9,8,7,6,5,4,3,2,1]
        sort_stack_recursive(s1)
        assert s1 == outputstack
        
if __name__ == "__main__":
	test_sort_stack()
	test_sort_stack_1_element()
	test_sort_stack_empty()
	test_sort_stack_big()
        test_sort_stack_recursive()
