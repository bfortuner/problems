from entry import Entry

"""
Implement Hashmap w Get, Put, and Remove operations

Questions:
1) What happens on Get if entry doesn't exist? Returns None? Or Throws Exception like Python dictionary?
2) What is Stored? And Entry helper class which can be extended?
3) 

"""

class HashMap:
	"""
	Naive implementation assuming no collisions
	"""
	def __init__(self, size):
		self.size = size
		self.buckets = [None for x in range(size)]  #need fixed size

	def put(self, key, value):
		entry = Entry(key, value)
		bucket_index = self.get_bucket(key)
		self.buckets[bucket_index] = entry

	def get(self, key):
		"""
		Returns value matching key 
		provided by caller
		"""
		bucket_index = self.get_bucket(key)
		entry = self.buckets[bucket_index]
		if not entry:
			return None
		return entry.value

	def remove(self, key):
		bucket_index = self.get_bucket(key)
		self.buckets[bucket_index] = None

	def get_bucket(self, key):
		"""
		Returns index of bucket in array (first bucket = 0)
		"""
		return self.hash_function(key, self.size) - 1

	def hash_function(self, key, num_of_buckets):
		"""
		Returns int from string within num_of_buckets (first bucket = 1)
		"""
		ord_sum = 0
		for s in key:
			ord_sum += ord(s)
		return ord_sum % num_of_buckets



#Tests

def test_get_buckets():
	hashmap = HashMap(10)
	buckets = hashmap.buckets
	assert len(buckets) == 10

def test_hash_function():
	hashmap = HashMap(10)
	assert hashmap.hash_function("A", hashmap.size) == 5
	assert hashmap.hash_function("F", hashmap.size) == 0
	assert hashmap.hash_function("AF", hashmap.size) == 5

def test_get_bucket():
	hashmap = HashMap(10)
	assert hashmap.get_bucket("A") == 4
	assert hashmap.get_bucket("F") == -1
	assert hashmap.get_bucket("AF") == 4

def test_basic_operations():
	hashmap = HashMap(10)
	hashmap.put("A","Brendan") #index 4
	assert hashmap.get("A") == "Brendan"
	hashmap.remove("A")
	assert hashmap.get("A") == None

if __name__ == "__main__":
	test_get_buckets()
	test_hash_function()
	test_get_bucket()
	test_basic_operations()

