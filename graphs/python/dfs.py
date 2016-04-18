from Vertex import Vertex
from Graph import Graph
from Graph import build_test_graph

def dfs_iterative(start, value_to_find):
	"""
	Input: starting vertex, value to find
	Output: return Vertex holding value_to_find, else None

	Graph is a digraph. So it has cycles. Values can repeat.
	"""
	to_visit_or_visited = set()
	to_visit = [] # Stack
	to_visit_or_visited.add(start)
	to_visit.append(start)
	while len(to_visit) > 0:
		vertex = to_visit.pop() #get val on top of stack
		if vertex.value == value_to_find:
			return vertex
		for neighbor in vertex.neighbors:
			if neighbor not in to_visit_or_visited:
				to_visit.append(neighbor)
				to_visit_or_visited.add(neighbor)
	return None

def dfs_recursive(vertex, value_to_find):
	vertex.status = "VISITED"
	if vertex.value == value_to_find:
		return vertex
	for neighbor in vertex.neighbors:
		if neighbor.status != "VISITED":
			result = dfs_recursive(neighbor, value_to_find)
			if result:
				return result
	return None


#Tests

def test_dfs_iterative():

	graph = build_test_graph()
	graph.pretty_print()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_iterative(v1,"B") == v2
	assert dfs_iterative(v1,"C") == v3
	assert dfs_iterative(v1,"D") == v4
	assert dfs_iterative(v1,"E") == v5

	assert dfs_iterative(v2,"A") == v1
	assert dfs_iterative(v3,"A") == v1
	assert dfs_iterative(v3,"E") == v5
	assert dfs_iterative(v3, "NOTHING") == None

def test_dfs_recursive():
	graph = build_test_graph()
	graph.pretty_print()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v1,"B") == v2

def test_dfs_recursive2():
	graph = build_test_graph()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v1,"C") == v3

def test_dfs_recursive3():
	graph = build_test_graph()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v1,"D") == v4

def test_dfs_recursive4():
	graph = build_test_graph()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v1,"E") == v5

def test_dfs_recursive5():
	graph = build_test_graph()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v2,"A") == v1

def test_dfs_recursive6():
	graph = build_test_graph()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v3, "NOTHING") == None

def test_dfs_recursive7():
	graph = build_test_graph()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert dfs_recursive(v3,"E") == v5

if __name__ == "__main__":
	test_dfs_iterative()
	test_dfs_recursive()
	test_dfs_recursive2()
	test_dfs_recursive3()
	test_dfs_recursive4()
	test_dfs_recursive5()
	test_dfs_recursive6()
	test_dfs_recursive7()