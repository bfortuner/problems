"""
Key-Value Entry Class
Alternatively I could use a tuple, list, or dict?
"""

class Entry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def to_string(self):
		return "(" + self.key + ", " + self.value + ")"  