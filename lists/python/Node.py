class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next


# Tests

def test_get_set_node():
	second_node = Node("B")
	head = Node("A", second_node)

	assert head.get_next() == second_node
	assert head.value == "A"

	head.set_value("Z")
	new_node = Node("C", second_node)
	head.set_next(new_node)

	assert head.value == "Z"
	assert head.get_next() == new_node

	next = head.get_next()
	assert next == new_node
	assert next.get_next() == second_node

	next = next.get_next()
	assert next == second_node
	assert next.get_next() is None

if __name__ == "__main__":
	test_get_set_node() 
