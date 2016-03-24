class DoublyNode:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next