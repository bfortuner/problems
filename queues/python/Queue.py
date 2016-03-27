from Node import Node

"""
Implement Queue w Linked List

Enqueue, Dequeue, Size methods
"""

class Queue(object):
	def __init__(self, head=None):
		self.head = head
		self.size = 0

	def enqueue(self, value):
		self.size += 1
		if self.head is None:
			self.head = Node(value)
			return
		cur_node = self.head
		while cur_node.next is not None:
			cur_node = cur_node.next
		cur_node.next = Node(value)

	def dequeue(self):
		if self.head is not None:
			value = self.head.value
			self.head = self.head.next
			self.size -= 1
			return value
		else:
			return None

	def get_size(self):
		return self.size



#Tests

def test_basic_ops():
	queue = Queue()
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