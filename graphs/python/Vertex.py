
class Vertex(object):
	"""
	Simple Vertex Implementation which stores its value
	and its neighboring Vertices
	"""

	def __init__(self, value=None, neighbors=None):
		self.value = value
		self.neighbors = neighbors if neighbors is not None else []

	def add_neighbor(self, neighbor):
		"""
		Input: Vertex obj to add to neighbors list
		"""
		self.neighbors.append(neighbor)

	def add_neighbors(self, neighbors):
		self.neighbors.extend(neighbors)

	def remove_neighbor(self, neighbor):
		"""
		Input: Vertex obj to remove from neighbors
		Output: Vertex obj removed or None
		"""
		i = 0
		for n in self.neighbors:
			if n is neighbor:
				return self.neighbors.pop(i)
			i+=1
		return None

	def id(self):
		"""
		Uniquely identifies an object. Could be stored in the
		neighbors list instead of storing the entire Neighbor object
		if we wanted to save space provided we had a way to lookup 
		the vertex in a hashmap elsewhere (in the Graph for instance)
		"""
		return id(self)

	def __repr__(self):
		return "(" + str(self.value) + ")"


# Tests

def test_basic_ops():
	vertex = Vertex("A")
	copy = vertex
	assert copy is vertex 
	assert copy == vertex
	assert vertex.id() == copy.id()
	print vertex

def test_add_remove_neighbor():
	vertex = Vertex("A")
	assert len(vertex.neighbors) == 0
	
	vertex2 = Vertex("B")
	vertex.add_neighbor(vertex2)
	assert len(vertex.neighbors) == 1
	assert vertex.neighbors[0] is vertex2

	copy_vertex_2 = vertex.remove_neighbor(vertex2)
	assert len(vertex.neighbors) == 0
	assert copy_vertex_2 is vertex2
	assert vertex.remove_neighbor(vertex2) == None
	assert len(vertex.neighbors) == 0

def test_add_neighbors():
	vertex1 = Vertex("A")
	vertex2 = Vertex("B")
	vertex3 = Vertex("C")

	vertex1.add_neighbors([vertex2,vertex3])
	assert len(vertex1.neighbors) == 2
	assert len(vertex2.neighbors) == 0
	assert len(vertex3.neighbors) == 0

	vertex4 = Vertex("F")
	assert len(vertex4.neighbors) == 0

	vertex2.add_neighbors([vertex1, vertex4, vertex3])
	assert len(vertex2.neighbors) == 3
	assert len(vertex1.neighbors) == 2
	assert len(vertex3.neighbors) == 0

if __name__ == "__main__":
	test_basic_ops()
	test_add_remove_neighbor()
	test_add_neighbors()