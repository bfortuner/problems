from entry import Entry

"""
Implement Hashmap w Get, Put, and Remove operations
Resolve collisions with "Open Addressing" technique

Steps
1) For Put, if collision, continue through buckets until next empty bucket found 
2) For Get, check if Key == Key, if not, continue until Key found or None found, if None return None
3) What if we run out of buckets? Chaining doesn't have this problem? 
    -We can set an enormously large amount of buckets
    -We can write a dynamically resizing algorithm
    -When do we resize?
    -If we resize that means we have to rehash everything in our HashTable (expensive! or not?)
4) What are some techniques for evenly distributing data across buckets?
    -More buckets (more possible modulos)
    -Better Hash algorithm
    -Perhaps if collisions, do "Rehash after appending Known Salt string to Key"
    -Instead of linear open addressing search, skip by 3, or by prime numbers, or by ???
"""

class HashTableAddressing:
	"""
	Resolve Collisions w Open Addressing
	Naive which simply scans linearly 1 by 1 until empty bucket is found
	"""
	def __init__(self, size):
		self.MIN_SIZE = 20
		self.MAX_ITEM_THRESHOLD_BEFORE_RESIZE = .9
		self.MIN_ITEM_THRESHOLD_BEFORE_RESIZE = .5
		self.RESIZE_UP_FACTOR = 2
		self.RESIZE_DOWN_FACTOR = .75
		self.size = size
		self.buckets = [None for x in range(size)]  #need fixed size

	def put(self, key, value, resizing=False):
		if not resizing:
			self.resize_if_required()
		entry = Entry(key, value)
		bucket_index = self.get_bucket(key)
		while self.buckets[bucket_index] != None and \
		self.buckets[bucket_index].key != key:
			if bucket_index == self.size-1:
				bucket_index = 0
			else:
				bucket_index += 1
		self.buckets[bucket_index] = entry

	def get(self, key):
		"""
		Returns value matching key 
		provided by caller
		"""
		bucket_index = self.get_bucket(key)
		while self.buckets[bucket_index] != None and \
		self.buckets[bucket_index].key != key:
			if bucket_index == self.size-1:
				bucket_index = 0
			else:
				bucket_index += 1
		if self.buckets[bucket_index] is None:
			return None
		return self.buckets[bucket_index].value

	def remove(self, key):
		self.resize_if_required()
		bucket_index = self.get_bucket(key)
		while self.buckets[bucket_index] != None and \
		self.buckets[bucket_index].key != key:
			if bucket_index == self.size-1:
				bucket_index = 0
			else:
				bucket_index += 1
		self.buckets[bucket_index] = None

	def get_bucket(self, key):
		"""
		Returns index of bucket in array (first bucket = 0)
		G = 0, H = 1, I = 2, A = 4
		"""
		return self.hash_function(key, self.size) - 1

	def hash_function(self, key, num_of_buckets):
		"""
		Returns int from string within num_of_buckets (first bucket = 1)
		ord("G") == 71 % 10 == 1
		ord("H") == 72 % 10 == 2
		ord("I") == 73 % 10 == 3
		"""
		ord_sum = 0
		for s in key:
			ord_sum += ord(s)
		return ord_sum % num_of_buckets

	def get_item_count(self):
		count = 0
		for item in self.buckets:
			if item:
				count += 1
		return count

	def print_hash_table(self):
		for item in self.buckets:
			if item is not None:
				print item.to_string()
			else:
				print "()"

	def resize(self, factor):
		self.size = int(round(self.size * factor))
		# oldbuckets references buckets
		oldbuckets = self.buckets
		assert oldbuckets is self.buckets
		# buckets breaks relationship through reassignment
		self.buckets = [None for x in range(self.size)]
		assert oldbuckets is not self.buckets
		for entry in oldbuckets:
			if entry:
				self.put(entry.key, entry.value, True)

	def resize_if_required(self):
		item_count_to_bucket_size_decimal = self.get_item_count() / float(self.size)
		if item_count_to_bucket_size_decimal > self.MAX_ITEM_THRESHOLD_BEFORE_RESIZE:
			print "resizing up"
			self.resize(self.RESIZE_UP_FACTOR)
		if self.size > self.MIN_SIZE and item_count_to_bucket_size_decimal < self.MIN_ITEM_THRESHOLD_BEFORE_RESIZE:
			print "Resizing down"
			self.resize(self.RESIZE_DOWN_FACTOR)



#Tests

def are_entries_equal(entry1, entry2):
	if entry1 == entry2:
		return True
	elif entry1 == None or entry2 == None:
		return False
	keys_equal = entry1.key == entry2.key
	values_equal = entry1.value == entry2.value
	return keys_equal and values_equal

def hash_tables_are_equal(h1, h2):
	if h1 == h2:
		return True
	elif h1 is None or h2 is None:
		return False
	elif len(h1.buckets) != len(h2.buckets):
		return False
	for i in range(len(h1.buckets)):
		if not are_entries_equal(h1.buckets[i],h2.buckets[i]):
			return False
	return True

def test_get_buckets():
	hashmap = HashTableAddressing(10)
	buckets = hashmap.buckets
	assert len(buckets) == 10

def test_hash_function():
	hashmap = HashTableAddressing(10)
	assert hashmap.hash_function("A", hashmap.size) == 5
	assert hashmap.hash_function("F", hashmap.size) == 0
	assert hashmap.hash_function("AF", hashmap.size) == 5

def test_get_bucket():
	hashmap = HashTableAddressing(10)
	assert hashmap.get_bucket("A") == 4
	assert hashmap.get_bucket("F") == -1
	assert hashmap.get_bucket("AF") == 4

def test_basic_operations():
	hashmap = HashTableAddressing(10)
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
	#G = 0, H = 1, I = 2, A = 4
	hashmap = HashTableAddressing(10)
	hashmap.put("G","1")
	hashmap.put("GG","2")
	hashmap.put("GGG","3")
	hashmap.put("A","4")
	hashmap.put("AAH","4")

	# print "Table Prior To Override"
	# hashmap.print_hash_table()

	hashmap.put("G","B")
	hashmap.put("GG","BB")
	hashmap.put("AAH","BBB")

	# print "Table After Override"
	# hashmap.print_hash_table()

	assert hashmap.get("G") == "B"
	assert hashmap.get("GG") == "BB"
	assert hashmap.get("AAH") == "BBB"


def test_put_remove_handling():
	#G = 0, H = 1, I = 2, A = 4
	hashmap = HashTableAddressing(10)
	hashmap.put("G","1")
	hashmap.put("GG","2")
	hashmap.put("GGG","3")
	hashmap.put("A","4")
	hashmap.put("AAH","4")

	# print "Table Prior To Override"
	# hashmap.print_hash_table()

	hashmap.put("G","B")
	hashmap.put("GG","BB")
	hashmap.put("AAH","BBB")

	# print "Table After Override"
	# hashmap.print_hash_table()

	assert hashmap.get("G") == "B"
	assert hashmap.get("GG") == "BB"
	assert hashmap.get("AAH") == "BBB"

	hashmap.remove("G")
	hashmap.remove("GG")
	hashmap.remove("AAH")

	assert hashmap.get("G") is None
	assert hashmap.get("GG") is None
	assert hashmap.get("AAH") is None

def test_are_hash_tables_equal():
	"""
	Order of insertion matters
	"""
	hashmap = HashTableAddressing(10)
	hashmap.put("A","B")
	hashmap.put("AF","K")

	hashmap2 = HashTableAddressing(10)
	hashmap2.put("A","B")
	hashmap2.put("AF","K")

	assert hash_tables_are_equal(hashmap, hashmap) == True
	assert hash_tables_are_equal(hashmap, None) == False
	assert hash_tables_are_equal(
		HashTableAddressing(2), HashTableAddressing(4)) == False
	assert hash_tables_are_equal(hashmap, hashmap2) == True

def test_get_item_count():
	hashmap = HashTableAddressing(10)
	assert hashmap.get_item_count() == 0

	hashmap.put("A","B")
	hashmap.put("AF","K")
	assert hashmap.get_item_count() == 2

	hashmap.remove("A")
	assert hashmap.get_item_count() == 1

def test_resizing():
	#G = 0, H = 1, I = 2, A = 4
	hashmap = HashTableAddressing(10)
	hashmap.put("G","1")
	hashmap.put("GG","2")
	hashmap.put("GGG","3")
	hashmap.put("A","4")
	hashmap.put("AAH","5")
	hashmap.put("GGGG","6")
	hashmap.put("GGGGG","7")
	hashmap.put("GGGGGG","8")
	hashmap.put("GGGGGGG","9")
	hashmap.put("GGGGGGGG","10")

	# print "------"
	# hashmap.print_hash_table()

	assert hashmap.size == 10
	assert hashmap.get_item_count() == 10

	#Previously this will trigger infinite loop
	hashmap.put("GGGGGGGGG","11")
	hashmap.put("GGGGGGGGGG","12")
	hashmap.put("GGGGGGGGGGG","13")

	assert hashmap.size == 20
	assert hashmap.get_item_count() == 13

	# print "------"
	# hashmap.print_hash_table()


def test_resizing_down():
	#G = 0, H = 1, I = 2, A = 4
	hashmap = HashTableAddressing(10)
	hashmap.put("G","1")
	hashmap.put("GG","2")
	hashmap.put("GGG","3")
	hashmap.put("A","4")
	hashmap.put("AAH","5")
	hashmap.put("GGGG","6")
	hashmap.put("GGGGG","7")
	hashmap.put("GGGGGG","8")
	hashmap.put("GGGGGGG","9")
	hashmap.put("GGGGGGGG","10")
	hashmap.MIN_SIZE = 5
	hashmap.MAX_ITEM_THRESHOLD_BEFORE_RESIZE = .9
	hashmap.MIN_ITEM_THRESHOLD_BEFORE_RESIZE = .5
	hashmap.RESIZE_UP_FACTOR = 2
	hashmap.RESIZE_DOWN_FACTOR = .5

	# print "------"
	# hashmap.print_hash_table()

	assert hashmap.size == 10
	assert hashmap.get_item_count() == 10

	hashmap.put("GGGGGGGGG","11")
	hashmap.put("GGGGGGGGGG","12")
	hashmap.put("GGGGGGGGGGG","13")

	assert hashmap.size == 20
	assert hashmap.get_item_count() == 13

	hashmap.remove("G")
	hashmap.remove("GG")
	hashmap.remove("GGG")
	hashmap.remove("A")
	hashmap.remove("AAH")
	hashmap.remove("GGGG")
	hashmap.remove("GGGGG")
	hashmap.remove("GGGGGG")
	hashmap.remove("GGGGGGG")
	hashmap.remove("GGGGGGGG")
	
	# print "------"
	# hashmap.print_hash_table()

	assert hashmap.size == 5
	assert hashmap.get_item_count() == 3

	hashmap.remove("GGGGGGGGGGG")
	hashmap.remove("GGGGGGGGG")

	assert hashmap.size == 5
	assert hashmap.get_item_count() == 1


if __name__ == "__main__":
	test_get_buckets()
	test_hash_function()
	test_get_bucket()
	test_basic_operations()
	test_put_collision_handling__overrides_existing_key()
	test_put_remove_handling()
	test_are_hash_tables_equal()
	test_get_item_count()
	test_resizing()
	test_resizing_down()
