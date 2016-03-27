from Node import Node

"""
Queue With Stacks

Implement a queue using 2 Stacks

Approaches
1) Main, Backup stack. For an enqueue, we just push to Main O(1). For a dequeue,
we Pop() everything from main onto Backup and return first element on back. O(n) Then swap stacks.  

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

	def is_empty(self):
		return self.head is None


class QueueWithStacks(object):
	def __init__(self):
		self.main = Stack()
		self.backup = Stack()

	def enqueue(self, value):
		self.main.push(value)

	def dequeue(self):
		if self.main.is_empty():
			return None
		while not self.main.is_empty():
			self.backup.push(self.main.pop())
		value = self.backup.pop()
		while not self.backup.is_empty():
			self.main.push(self.backup.pop())
		return value

	def get_size(self):
		return self.main.size()

"""

Main = 3 --> 2
Backup = 2 --> 3
val = 1


"""


#Tests

def test_basic_ops():
	queue = QueueWithStacks()
	assert queue.get_size() == 0
	assert queue.dequeue() == None
	queue.enqueue(5)
	assert queue.get_size() == 1
	assert queue.dequeue() == 5
	assert queue.get_size() == 0
	assert queue.dequeue() == None

	queue.enqueue(5)
	queue.enqueue(5)
	queue.enqueue(5)
	assert queue.get_size() == 3


if __name__ == "__main__":
	test_basic_ops()