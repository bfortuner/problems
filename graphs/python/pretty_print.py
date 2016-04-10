from Graph import Graph
from Graph import build_test_graph
from Vertex import Vertex

"""
Pretty Print

Starting with a single Vertex, implement a method that prints out a 
string representation of a Graph that resembles a visual web 

Approach:
1) Using BFS, extract all unique vertices from the graph into set
2) Loop through vertices, plot each vertex into a arbitrary coordinates in matrix
3) Rearrange vertices in matrix until correctly positions
4) Pass matrix into format string method to print output 

"""

def extract_vertices(vertex):
	"""
	Input: starting Vertex, value to find
	Output: return closest Vertex that contains value

	Graph is a digraph. So it has cycles. Values can repeat.
	"""
	neighbors = []
	visited = set() #all unique elements
	neighbors.append(vertex)
	while len(neighbors) > 0:
		vertex = neighbors.pop(0)
		for neighbor in vertex.neighbors:
			if neighbor not in visited:
				neighbors.append(neighbor)
				visited.add(neighbor)
	return visited

def plot_to_array(vertices):
	return []

def pretty_print(vertices_arr=[]):
	print vertices_arr



def test_pretty_print():
	graph = build_test_graph()
	graph.pretty_print()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	vertices_set = extract_vertices(graph.vertices[0])
	print vertices_set

if __name__ == "__main__":
	test_pretty_print()

