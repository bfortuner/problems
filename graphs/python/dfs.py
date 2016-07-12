from Graph import Graph
from Graph import build_test_graph
from Vertex import Vertex

"""
These methods take a vertex as a starting 
point. If some nodes aren't connected to any
others, this won't work, you would need to take
the Graph as input and loop through the vertices
"""

def dfs(vertex,value,visited):
        for n in vertex.neighbors:
                if n not in visited:
                        visited.add(n)
                        result = dfs(n,value,visited)
                        if result != None:
                                return result
        if vertex.key == value:
                return vertex
        return None

def dfs_recursive(vertex, value):
	"""
	Input: starting Vertex, value to find
	Output: return first Vertex that contains value

	Graph is a digraph. So it has cycles. Values can repeat.
	"""
	visited = set()
        return dfs(vertex,value,visited)

def dfs_iterative(vertex, value):
        visited = set()
        stack = []
        stack.append(vertex)
        while len(stack) > 0:
                vertex = stack.pop()
                if vertex.key == value:
                        return vertex
                for n in vertex.neighbors:
                        if n not in visited:
                                visited.add(n)
                                stack.append(n)
        return None



## Tests

def test_dfs_recursive():
	graph = build_test_graph()
	print graph

	vertices = graph.vertices
	v1 = vertices["A"]
	v2 = vertices["B"]
	v3 = vertices["C"]
	v4 = vertices["D"]
	v5 = vertices["E"]

	assert dfs_recursive(v1,"B") == v2
	assert dfs_recursive(v1,"C") == v3
	assert dfs_recursive(v1,"D") == v4
	assert dfs_recursive(v1,"E") == v5

	assert dfs_recursive(v2,"A") == v1
	assert dfs_recursive(v3,"A") == v1
	assert dfs_recursive(v3,"E") == v5

def test_dfs_iterative():
	graph = build_test_graph()
	print graph

	vertices = graph.vertices
	v1 = vertices["A"]
	v2 = vertices["B"]
	v3 = vertices["C"]
	v4 = vertices["D"]
	v5 = vertices["E"]

	assert dfs_iterative(v1,"B") == v2
	assert dfs_iterative(v1,"C") == v3
	assert dfs_iterative(v1,"D") == v4
	assert dfs_iterative(v1,"E") == v5

	assert dfs_iterative(v2,"A") == v1
	assert dfs_iterative(v3,"A") == v1
	assert dfs_iterative(v3,"E") == v5

if __name__ == "__main__":
	test_dfs_recursive()
        test_dfs_iterative()

