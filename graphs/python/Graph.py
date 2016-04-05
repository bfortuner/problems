from Vertex import Vertex

class Graph(object):
	"""
	Simple Adjacency List Implementation Where Graph
	Keeps Master List of All Vertices and Each Vertex 
	Keeps and List of All its Neighbors
	"""
	def __init__(self, vertices=[]):
		self.vertices=vertices

	#Add vertex
	#Remove vertex (loop through and remove all edges)
	#Could I store edges in HashMap? Or in Vertices?
	#Bi-directional or uni-directional? Unidirectional is a Tree?

	def pretty_print(self):
		for vertex in self.vertices:
			print str(vertex.value) + " " + str(vertex.neighbors)



def build_test_graph():
	"""
	A --> B <->
	^     |    |
	D <-> C -> E
	"""
	v1 = Vertex("A")
	v2 = Vertex("B")
	v3 = Vertex("C")
	v4 = Vertex("D")
	v5 = Vertex("E")

	v1.add_neighbor(v2)
	v2.add_neighbors([v3,v5])
	v3.add_neighbors([v2,v4,v5])
	v4.add_neighbors([v1,v3])
	v5.add_neighbors([v2])
	
	return Graph([v1,v2,v3,v4,v5])


# Tests

def test_basic_ops():
	vertex = Vertex("A")
	vertex2 = Vertex("B")
	vertex3 = Vertex("C")

def test_build_test_graph():
	test_graph = build_test_graph()
	test_graph.pretty_print()


if __name__ == "__main__":
	test_basic_ops()
	test_build_test_graph()