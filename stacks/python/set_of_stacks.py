from Stack import Stack
from Stack import build_stack_from_list

"""
Set of Stacks

Consider a Stack of plates. If one stack gets too high, create a new 
stack of plates. Implement a special stack that holds these multiple 
stacks. When the first stack passes some threshold, the class creates 
a new stack and continues. Implement both Push and Pop methods.

Approach
-Keep list of stacks
-Keep threshold CONSTANT
-Always draw from stacks[0] - first stack
-Keep min number of stacks = 0
-Push Operation - For each push method, check size of current stack, 
if > THRESHOLD, add stack then complete stacks[0]push(val)
-Pop Method - Pop from stacks[0].pop(). If len(stacks) > 1 and stacks[0].size() == 0
del stacks[0]

"""

class SetOfStacks(object):
	def __init__(self):
		self.stacks = [Stack()] #initialize w one stack
		self.MAX_ITEM_THRESHOLD = 3

	def push(self, value):
		self.update_stacks_push()
		self.stacks[0].push(value)

	def pop(self):
		self.update_stacks_pop()
		return self.stacks[0].pop()

	def update_stacks_push(self):
		"""
		If the "active" stack is FULL, add a new stack to the
		top of our stack pool
		"""
		if self.stacks[0].size() == self.MAX_ITEM_THRESHOLD:
			new_stack = Stack()
			self.stacks.insert(0,new_stack)

	def update_stacks_pop(self):
		"""
		If the size of the first stack (the "active" stack) is 0 
		and the client is trying to pop the top item, then we need to move
		to our backup stacks. BUT only do this if there is more than 1 stack
		"""
		if self.stacks[0].size() == 0 and len(self.stacks) > 1:
			self.stacks.pop(0)



def test_basic_ops():
	stack = SetOfStacks()
	assert stack.pop() == None
	assert len(stack.stacks) == 1
	test_values = [1,2,3,4,5,6,7]
	for val in test_values:
		stack.push(val)
		print "num of stacks: " + str(len(stack.stacks))

	answer_values = [7,6,5,4,3,2,1]
	for val in answer_values:
		assert stack.pop() == val
		print "num of stacks: " + str(len(stack.stacks))

	assert stack.pop() == None
	stack.pop()
	assert stack.pop() == None
	assert len(stack.stacks) == 1

if __name__ == "__main__":
	test_basic_ops()
