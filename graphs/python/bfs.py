
def bsf(vertex, value):
	"""
	Input: starting vertex, value to find
	Output: return closest vertex that contains value

	Graph is a digraph. So it has cycles. Values can repeat.
	"""
	neighbors = []
	visited = Set() #all unique elements
	neighbors.append(vertex)
	while len(neighbors) > 0:
		vertex = neighbors.pop(0)
		if vertex.value == value:
			return vertex
		for neighbor in vertex.neighbors:
			if neighbor not in visited:
				neighbors.append(neighbor)
				visited.add(neighbor)
	return None




def test_bfs():
	


if __name__ == "__main__":

