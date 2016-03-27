from Stack import Stack
from Node import Node
"""
Stacks with Array

Implement 3 stacks using a single array

Approaches
1) Index 0, 3, 6.. first stack. 1, 4, 7.. second stack. 2, 5, 8.. third stack.

"""

class StacksWithArray(object):
	def __init__(self):
		self.array = [None for x in range(99)]
		# Represent next available open position
		self.stack_positions = {
			0 : 0,
			1 : 1,
			2 : 2
		}
		self.INCREMENT = 3

	def push(self, stackno, value):
		"""
		Find the current open position in array
		of the stack (0-2) requested by client
		Add value, then increment to next open position
		"""
		index = self.stack_positions[stackno]
		self.array[index] = value
		self.stack_positions[stackno] += self.INCREMENT
		print "stack positions = " + str(self.stack_positions)
		print "array values = " + str(self.array)

	def pop(self, stackno):
		index = self.stack_positions[stackno]
		if index > stackno:
			self.stack_positions[stackno] -= self.INCREMENT
			index = self.stack_positions[stackno]
		value = self.array[index]
		self.array[index] = None
		print "stack positions = " + str(self.stack_positions)
		print "array values = " + str(self.array)
		return value



#Tests

def test_basic_ops():
	stack = StacksWithArray()
	stack.push(0,"A")
	stack.push(1,"B")
	stack.push(2,"C")

	stack.push(0,"A")
	stack.push(0,"A")
	stack.push(0,"A")

	stack.pop(0)
	stack.pop(0)
	stack.pop(0)

	stack.push(0,"A")
	stack.pop(1)
	stack.pop(1)
	stack.pop(1)
	stack.pop(2)
	stack.pop(2)
	stack.pop(0)
	stack.pop(0)
	stack.pop(0)


if __name__ == "__main__":
	test_basic_ops()
