class Location:
	def __init__(hasLocker=False, neighbors=[]):
		this.hasLocker = hasLocker
		this.neighbors = neighbors

	def hasLocker():
		return this.hasLocker

	def get_neighbors():
		return this.neighbors

	def add_neighbor(location):
		this.neighbors.append(location)


def find_nearest_locker(location):
	visited =[]
	neighbors = location.get_neighbors()
	for neighbor in neighbors:
		if neighbor not in visited and neighbor.has_locker():
			return neighbor
		else:
			visited.append(neighbor)	
			neighbors.extend(neighbor.get_neighbors())
	return None

def test_find_nearest_locker():
	l3a = Location(True, [l2b])
	l3b = Location(False,[l2a,l2b])
	l3c = Location(False,[l2c])

	l2b = Location(False, [l1,l2a,l3b,l3a])
	l2a = Location(False, [l1,l2b,l2c])
	l2c = Location(False, [l1,l2a,l3c])

	l1 = Location(False, [l2a,l2b,l2c])

	print find_nearest_locker(l1) == l3a
	assert find_nearest_locker(l1) == l3a

test_find_nearest_locker()



class Location:
	def __init__(hasLocker=False, neighbors=[]):
		this.hasLocker = hasLocker
		this.neighbors = neighbors #{'neighbor':neighbor, distance:5}

	def hasLocker():
		return this.hasLocker

	def get_neighbors():
		return this.neighbors

	def add_neighbor(location):
		this.neighbors.append(location)

def find_nearest_locker_distance(location):
	closest_neighbor = location
	closest_distance = 0
	visited =[]
	neighbor = location.get_neighbors()
	for neighbor in neighbors:
		if road not in visited:
			#check all the neighbors
			#if neighbor has locker
			return neighbor
		else:
			visited.append(neighbor)	
			neighbors.extend(neighbor.get_neighbors())
	return None

def test_find_nearest_locker():
	l3a = Location(True, [l2b])
	l3b = Location(False,[l2a,l2b])
	l3c = Location(False,[l2c])

	l2b = Location(False, [l1,l2a,l3b,l3a])
	l2a = Location(False, [l1,l2b,l2c])
	l2c = Location(False, [l1,l2a,l3c])

	l1 = Location(False, [l2a,l2b,l2c])

	print find_nearest_locker(l1) == l3a
	assert find_nearest_locker(l1) == l3a

test_find_nearest_locker()


