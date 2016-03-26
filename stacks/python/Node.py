

class Node(object):
	"""
	Python 2 need to inherit from object
	Python 3 inherit from object is implicit
	"""
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next
