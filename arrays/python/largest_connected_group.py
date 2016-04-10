"""
Largest Connected Group

Given 2D array of X/-, find the size of the largest connected group of X's
	x x - -
	x - - -
	x - - x
	- - x -

	- x x -
	- x - -
	- x - x
	- - x -

Cases:
1) All X or -
2) Do diagnals count?
3) Two equal groups?
4) Group in the middle

Approach
1) BFS - Starting at top left, loop through 2x2 array and begin search
2) Keep track of nodes visited (by using Set or Storing in another matrix copy)
3) Keep track of max size at the top
---
Create Helper Class called Graph
1) Stores the Array
2) Stores the Visited Array Copy
3) Has Helper Method is coordinate in graph
4) Get left neighbor, get right neighbor, get above neighbor, get below neighbor
5) Has Helper Method get X neighbors
6) Keep getting the X neighbors until exhaust (neighbors queue is empty)
7) For each neighbor found, increment the local_x_neighbor_count
8) If local x_neighbor_count > max_x_neighbor_count, then set max_neighbor count
"""

class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(" + str(self.x) + \
			"," + str(self.y) + ")"

class Graph(object):
	def __init__(self, matrix):
		self.matrix = matrix
		self.visited = self.build_visited()

	def build_visited(self):
		num_of_rows = len(self.matrix)
		num_of_cols = len(self.matrix[0])
		visited = []
		for row in range(num_of_rows):
			visited.append([0 for x in range(num_of_cols)])
		return visited

	def was_visited(self, coord):
		return self.visited[coord.y][coord.x] == 1

	def mark_visited(self, coord):
		self.visited[coord.y][coord.x] = 1

	def is_x(self, coord):
		return self.matrix[coord.y][coord.x] == 1

	def in_graph(self, coord):
		if coord.x < 0 or coord.y < 0:
			return False
		elif coord.x >= len(self.matrix[0]):
			return False
		elif coord.y >= len(self.matrix):
			return False
		return True

	def get_neighbors(self, coord):
		#print "getting neighbors of coord " + str(coord)
		neighbors = []
		left = Coordinate(coord.x-1, coord.y)
		right = Coordinate(coord.x+1, coord.y)
		above = Coordinate(coord.x, coord.y+1)
		below = Coordinate(coord.x, coord.y-1)
		for coordinate in [left,right,above,below]:
			if self.in_graph(coordinate):
				neighbors.append(coordinate)
		return neighbors

	def get_x_neighbors(self, coord):
		#print "Getting x neighbors of coord " + str(coord)
		x_neighbors = []
		neighbors = self.get_neighbors(coord)
		for coordinate in neighbors:
			x = coordinate.x
			y = coordinate.y
			if self.matrix[y][x] == 1:
				x_neighbors.append(coordinate)
		return x_neighbors

def get_group_size(graph, start_coord):
	print "getting group size of start_coord " + str(start_coord)
	group_size = 0
	x_neighbors = []
	x_neighbors.append(start_coord)
	while len(x_neighbors) > 0:
		coord = x_neighbors.pop(0)
		graph.mark_visited(coord)
		group_size+=1
		neighbors = graph.get_x_neighbors(coord)
		for neighbor in neighbors:
			if not graph.was_visited(neighbor):
				x_neighbors.append(neighbor)
	return group_size

def get_max_group_size(matrix):
	max_group_size = 0
	graph = Graph(matrix)
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			coord = Coordinate(x,y)
			if graph.is_x(coord) and not graph.was_visited(coord):
				local_group_size = get_group_size(graph, coord)
				if local_group_size > max_group_size:
					max_group_size = local_group_size
	return max_group_size


#Tests

matrix=[
 [1,1,0,0],
 [1,0,0,0],
 [1,0,0,1],
 [0,0,1,0]
]

matrix2=[
 [1,0,1,0],
 [0,1,1,0],
 [0,1,0,1],
 [1,1,1,0]
]

matrix3=[
 [1,0,1],
 [0,1,1],
 [0,1,0]
]

matrix_copy=[
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]
]

def test_get_visited():
	graph = Graph(matrix)
	assert graph.visited == matrix_copy

def test_get_neighbors():
	graph = Graph(matrix)
	print "getting neighbors"
	print graph.get_neighbors(Coordinate(2,2))
	print graph.get_neighbors(Coordinate(0,0))
	print graph.get_neighbors(Coordinate(1,2))

def test_get_x_neighbors():
	graph = Graph(matrix)
	print graph.get_x_neighbors(Coordinate(2,2))
	print graph.get_x_neighbors(Coordinate(0,0))

	graph = Graph(matrix2)
	print graph.get_x_neighbors(Coordinate(2,0))
	print graph.get_x_neighbors(Coordinate(2,1))
	print graph.get_x_neighbors(Coordinate(1,3))

def test_get_group_size():
	graph = Graph(matrix)
	assert get_group_size(graph, Coordinate(0,0)) == 4 
	graph = Graph(matrix)
	assert get_group_size(graph, Coordinate(3,2)) == 1
	graph = Graph(matrix)
	assert get_group_size(graph, Coordinate(2,3)) == 1

	graph2 = Graph(matrix2)
	assert get_group_size(graph2, Coordinate(0,0)) == 1
	graph2 = Graph(matrix2)
	assert get_group_size(graph2, Coordinate(2,0)) == 7

def test_get_max_group_size():
	assert get_max_group_size(matrix) == 4
	assert get_max_group_size(matrix2) == 7
	assert get_max_group_size(matrix3) == 4

if __name__ == "__main__":
 	test_get_visited()
 	test_get_neighbors()
 	test_get_x_neighbors()
 	test_get_group_size()
 	test_get_max_group_size()