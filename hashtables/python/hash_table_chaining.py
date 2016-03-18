from entry import Entry

"""
Implement Hashmap w Get, Put, and Remove operations
Resolve collisions with "Chaining" technique
"""

class HashTableChaining:
	"""
	Uses "chaining" to resolve collisions 
	"""
	def __init__(self, size):
		self.size = size
		self.buckets = [[] for x in range(size)]  #need fixed size actually

	def put(self, key, value):
		new_entry = Entry(key, value)
		bucket_index = self.get_bucket(key)
		bucket = self.buckets[bucket_index]
		for entry in bucket:
			if entry.key == key:
				entry.value = value
				return
		bucket.append(new_entry)

	def get(self, key):
		"""
		Returns value matching key 
		provided by caller
		"""
		bucket_index = self.get_bucket(key)
		bucket = self.buckets[bucket_index]
		for entry in bucket:
			if entry.key == key:
				return entry.value
		return None

	def remove(self, key):
		bucket_index = self.get_bucket(key)
		bucket = self.buckets[bucket_index]
		for i in range(len(bucket)):
			if bucket[i].key == key:
				del bucket[i]
				return

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

	def get_item_count(self):
		count = 0
		for b in self.buckets:
			count += len(b)
		return count

	def print_hash_table(self):
		for b in self.buckets:
			bucket_str = "["
			for item in b:
				bucket_str += item.to_string() + ","
			print bucket_str + "]"



#Tests

def hash_tables_are_equal(h1, h2):
	if h1 == h2:
		return True
	elif h1 is None or h2 is None:
		return False
	elif len(h1.buckets) != len(h2.buckets):
		return False
	for i in range(len(h1.buckets)):
		if not are_buckets_equal(h1.buckets[i],h2.buckets[i]):
			return False
	return True

def are_buckets_equal(b1_list, b2_list):
	"""
	Order of insertion matters
	"""
	if b1_list == b2_list:
		return True
	elif b1_list == None or b2_list == None:
		return False
	elif len(b1_list) != len(b2_list):
		return False
	for i in range(len(b1_list)):
		if b1_list[i].key != b2_list[i].key:
			return False
		if b1_list[i].value != b2_list[i].value:
			return False
	return True

def test_get_buckets():
	hashmap = HashTableChaining(10)
	buckets = hashmap.buckets
	assert len(buckets) == 10

def test_hash_function():
	hashmap = HashTableChaining(10)
	assert hashmap.hash_function("A", hashmap.size) == 5
	assert hashmap.hash_function("F", hashmap.size) == 0
	assert hashmap.hash_function("AF", hashmap.size) == 5

def test_get_bucket():
	hashmap = HashTableChaining(10)
	assert hashmap.get_bucket("A") == 4
	assert hashmap.get_bucket("F") == -1
	assert hashmap.get_bucket("AF") == 4

def test_basic_operations():
	hashmap = HashTableChaining(10)
	hashmap.put("A","Brendan") #index 4
	assert hashmap.get("A") == "Brendan"
	hashmap.remove("A")
	assert hashmap.get("A") == None

def test_are_buckets_equal():
	assert are_buckets_equal([],[]) == True
	assert are_buckets_equal([],None) == False
	assert are_buckets_equal([Entry("A","B"),Entry("B","C")],[Entry("A","B")]) == False
	assert are_buckets_equal([Entry("A","B")],[Entry("A","B")]) == True
	assert are_buckets_equal([Entry("A","B")],[Entry("A","C")]) == False
	assert are_buckets_equal([Entry("A","B"),Entry("B","C")],[Entry("A","B"),Entry("B","C")]) == True

def test_put_collision_handling__overrides_existing_key():
	answer_bucket = [Entry("A","C"), Entry("AF","K")]

	hashmap = HashTableChaining(10)
	hashmap.put("A","B")
	hashmap.put("AF","K")

	# print "Table Prior To Override"
	# hashmap.print_hash_table()

	hashmap.put("A","C")

	# print "Table After Override"
	# hashmap.print_hash_table()

	assert hashmap.get("A") == "C"
	assert hashmap.get("AF") == "K"

	buckets = hashmap.buckets
	for b in buckets:
		if len(b) == 2:
			assert are_buckets_equal(b, answer_bucket)

def test_are_hash_tables_equal():
	"""
	Order of insertion matters
	"""
	hashmap = HashTableChaining(10)
	hashmap.put("A","B")
	hashmap.put("AF","K")

	hashmap2 = HashTableChaining(10)
	hashmap2.put("A","B")
	hashmap2.put("AF","K")

	assert hash_tables_are_equal(hashmap, hashmap) == True
	assert hash_tables_are_equal(hashmap, None) == False
	assert hash_tables_are_equal(
		HashTableChaining(2), HashTableChaining(4)) == False
	assert hash_tables_are_equal(hashmap, hashmap2) == True

def test_get_item_count():
	hashmap = HashTableChaining(10)
	assert hashmap.get_item_count() == 0

	hashmap.put("A","B")
	hashmap.put("AF","K")
	assert hashmap.get_item_count() == 2

	hashmap.remove("A")
	assert hashmap.get_item_count() == 1

if __name__ == "__main__":
	test_get_buckets()
	test_hash_function()
	test_get_bucket()
	test_basic_operations()
	test_are_buckets_equal()
	test_put_collision_handling__overrides_existing_key()
	test_are_hash_tables_equal()
	test_get_item_count()

